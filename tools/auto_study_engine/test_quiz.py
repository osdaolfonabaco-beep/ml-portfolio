#!/usr/bin/env python3
#!/usr/bin/env python3
"""
Integration tester for the Auto Study Engine system.
Generates flashcards from Python source code and runs the quiz system.
"""

import os
import sys
import logging
import traceback

# Configure detailed logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(sys.stdout),
        logging.FileHandler('test_quiz_debug.log')
    ]
)
logger = logging.getLogger(__name__)

def setup_environment():
    """Set up the environment with proper paths"""
    # Get the absolute path to the project root
    project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    logger.debug(f"Project root: {project_root}")
    
    # Add project root to Python path
    sys.path.insert(0, project_root)
    
    # Create data directory if it doesn't exist
    data_dir = os.path.join(project_root, 'data')
    os.makedirs(data_dir, exist_ok=True)
    logger.debug(f"Data directory: {data_dir}")
    
    return project_root, data_dir

def main():
    """Main integration test function"""
    try:
        logger.info("Starting Auto Study Engine integration test")
        
        # Set up environment
        project_root, data_dir = setup_environment()
        
        # Import modules (doing this after path setup)
        try:
            from tools.auto_study_engine.agent_claude import generate_flashcards_from_code
            from tools.auto_study_engine.flashcore import save_deck, load_deck
            from tools.auto_study_engine.quizme import run_quiz
            logger.debug("All modules imported successfully")
        except ImportError as e:
            logger.error(f"Import error: {e}")
            logger.error(traceback.format_exc())
            return False
        
        # Define source code path
        source_code_path = os.path.join(
            project_root, 'foundations', 'python_advanced', 'lista_compras.py'
        )
        logger.debug(f"Source code path: {source_code_path}")
        
        # Verify source code exists
        if not os.path.exists(source_code_path):
            logger.error(f"Source code not found at: {source_code_path}")
            return False
        
        # Generate flashcards from source code
        logger.info("Generating flashcards from source code...")
        deck = generate_flashcards_from_code(source_code_path)
        
        if not deck:
            logger.error("Failed to generate flashcards")
            return False
        
        logger.debug(f"Generated deck with {len(deck)} flashcards")
        
        # Save deck to file
        deck_path = os.path.join(data_dir, 'mi_deck.json')
        logger.debug(f"Saving deck to: {deck_path}")
        
        try:
            save_deck(deck, deck_path)
            logger.info("Deck saved successfully")
        except Exception as e:
            logger.error(f"Error saving deck: {e}")
            logger.error(traceback.format_exc())
            return False
        
        # Verify file was created
        if not os.path.exists(deck_path):
            logger.error("Deck file was not created")
            return False
        
        # Load deck back from file
        logger.info("Loading deck from file...")
        try:
            loaded_deck = load_deck(deck_path)
            logger.debug(f"Loaded deck with {len(loaded_deck)} flashcards")
        except Exception as e:
            logger.error(f"Error loading deck: {e}")
            logger.error(traceback.format_exc())
            return False
        
        # Run quiz system (only if not in CI environment)
        if not os.getenv('CI'):
            logger.info("Starting quiz system...")
            try:
                run_quiz(loaded_deck)
                logger.info("Quiz completed successfully")
            except Exception as e:
                logger.error(f"Error running quiz: {e}")
                logger.error(traceback.format_exc())
                return False
        else:
            logger.info("Skipping interactive quiz in CI environment")
        
        logger.info("Integration test completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"Unexpected error in integration test: {e}")
        logger.error(traceback.format_exc())
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

    