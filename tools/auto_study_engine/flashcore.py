import json
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def save_deck(deck, file_path):
    """
    Save a flashcard deck to a JSON file.
    
    Args:
        deck (list): List of flashcards to save
        file_path (str): Path to the output JSON file
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        # Ensure directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        # Prepare deck with metadata
        deck_data = {
            "metadata": {
                "version": "1.0",
                "card_count": len(deck),
                "generator": "Auto Study Engine"
            },
            "cards": deck
        }
        
        # Write to file
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(deck_data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Deck saved successfully to {file_path}")
        return True
        
    except Exception as e:
        logger.error(f"Error saving deck to {file_path}: {e}")
        return False

def load_deck(file_path):
    """
    Load a flashcard deck from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        list: List of flashcards, or empty list if error
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Handle both old format (just array) and new format (with metadata)
        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and "cards" in data:
            return data["cards"]
        else:
            logger.error(f"Unexpected deck format in {file_path}")
            return []
            
    except FileNotFoundError:
        logger.error(f"Deck file not found: {file_path}")
        return []
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON from {file_path}: {e}")
        return []
    except Exception as e:
        logger.error(f"Error loading deck from {file_path}: {e}")
        return []