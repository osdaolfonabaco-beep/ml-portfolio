#!/usr/bin/env python3
"""
Quiz Engine for Auto Study Engine
Interactive quiz system with scoring and explanations
"""

import random
import logging

logger = logging.getLogger(__name__)

def run_quiz(flashcards):
    """
    Run an interactive quiz with the provided flashcards
    
    Args:
        flashcards (list): List of flashcard dictionaries
    """
    if not flashcards:
        print("❌ No flashcards available for quiz!")
        return
    
    print(f"🎯 Starting quiz with {len(flashcards)} flashcards...")
    print("=" * 50)
    
    score = 0
    total_possible = 0
    
    # Shuffle flashcards for variety
    random.shuffle(flashcards)
    
    for i, card in enumerate(flashcards, 1):
        print(f"\n📝 Question {i}/{len(flashcards)}")
        print(f"Category: {card.get('category', 'General')}")
        print(f"Difficulty: {card.get('difficulty', 'Medium')}")
        print(f"\n❓ {card['question']}")
        
        # Two attempts system
        for attempt in range(2):
            user_answer = input(f"\nYour answer (attempt {attempt + 1}/2): ").strip()
            
            if user_answer.lower() in card['answer'].lower():
                if attempt == 0:
                    points = 2  # Full points for first try
                    print("✅ Correct! +2 points")
                else:
                    points = 1  # Half points for second try
                    print("✅ Correct on second try! +1 point")
                
                score += points
                total_possible += 2
                break
            else:
                if attempt == 0:
                    print("❌ Incorrect. Try again...")
                else:
                    print("❌ Incorrect again.")
                    total_possible += 2
        else:
            # This runs if both attempts failed
            print(f"\n💡 Explanation: {card['answer']}")
        
        print("-" * 50)
    
    # Calculate final score
    if total_possible > 0:
        percentage = (score / total_possible) * 100
        print(f"\n🎉 Quiz completed!")
        print(f"Final score: {score}/{total_possible} ({percentage:.1f}%)")
    else:
        print("\n📊 No questions were scored.")
    
    return score

def test_quiz_system():
    """Test function for the quiz system"""
    test_cards = [
        {
            "question": "What does MLOps stand for?",
            "answer": "Machine Learning Operations",
            "category": "MLOps",
            "difficulty": "easy"
        },
        {
            "question": "What is CI/CD?",
            "answer": "Continuous Integration and Continuous Deployment",
            "category": "DevOps",
            "difficulty": "medium"
        }
    ]
    
    print("🧪 Testing quiz system...")
    run_quiz(test_cards)

if __name__ == "__main__":
    test_quiz_system()