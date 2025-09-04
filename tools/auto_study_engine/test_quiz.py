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

def verify_source_code(project_root):
    """Verify that source code files exist"""
    source_code_path = os.path.join(project_root, 'foundations', 'python_advanced', 'lista_compras.py')
    logger.debug(f"Checking source code at: {source_code_path}")
    
    if not os.path.exists(source_code_path):
        logger.error(f"❌ Source code not found at: {source_code_path}")
        logger.error("Available files in foundations/python_advanced/:")
        foundations_dir = os.path.join(project_root, 'foundations', 'python_advanced')
        if os.path.exists(foundations_dir):
            for file in os.listdir(foundations_dir):
                logger.error(f"  - {file}")
        else:
            logger.error("Foundations directory doesn't exist!")
        return False
    
    logger.info(f"✅ Source code found: {source_code_path}")
    return True

def main():
    """Main integration test function"""
    try:
        logger.info("🚀 Starting Auto Study Engine integration test")
        
        # Set up environment
        project_root, data_dir = setup_environment()
        
        # Verify source code exists
        if not verify_source_code(project_root):
            return False
        
        # Import modules (doing this after path setup)
        try:
            from tools.auto_study_engine.agent_claude import generate_flashcards_from_code
            from tools.auto_study_engine.flashcore import save_deck, load_deck
            logger.debug("✅ All modules imported successfully")
        except ImportError as e:
            logger.error(f"❌ Import error: {e}")
            logger.error(traceback.format_exc())
            return False
        
        # Define source code path
        source_code_path = os.path.join(
            project_root, 'foundations', 'python_advanced', 'lista_compras.py'
        )
        
        # Generate flashcards from source code
        logger.info("🔄 Generating flashcards from source code...")
        deck = generate_flashcards_from_code(source_code_path)
        
        if not deck:
            logger.error("❌ Failed to generate flashcards - empty deck returned")
            return False
        
        logger.info(f"✅ Generated {len(deck)} flashcards")
        
        # Save deck to file
        deck_path = os.path.join(data_dir, 'mi_deck.json')
        logger.debug(f"💾 Saving deck to: {deck_path}")
        
        try:
            save_deck(deck, deck_path)
            logger.info("✅ Deck saved successfully")
        except Exception as e:
            logger.error(f"❌ Error saving deck: {e}")
            logger.error(traceback.format_exc())
            return False
        
        # Verify file was created
        if not os.path.exists(deck_path):
            logger.error("❌ Deck file was not created!")
            return False
        
        # Check file size
        file_size = os.path.getsize(deck_path)
        logger.info(f"📊 Deck file size: {file_size} bytes")
        
        if file_size == 0:
            logger.error("❌ Deck file is empty!")
            return False
        
        logger.info("🎉 Integration test completed successfully!")
        return True
        
    except Exception as e:
        logger.error(f"💥 Unexpected error in integration test: {e}")
        logger.error(traceback.format_exc())
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        logger.error("❌ Integration test failed!")
    sys.exit(0 if success else 1)
