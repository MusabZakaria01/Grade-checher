# Grade Checker - My First Python Project
# Created by Musab - 2026

def check_grade():
    print("--- Welcome to Grade Checker ---")
    print("--- مرحبا بك في حاسبة الدرجات ---")
    
    try:
        grade = int(input("Enter your grade (0-100): "))
        
        if grade >= 90:
            print("🎉 Excellent! ممتاز")
        elif grade >= 80:
            print("👏 Very Good! جيد جدا")
        elif grade >= 70:
            print("👍 Good! جيد")
        elif grade >= 50:
            print("🙂 Pass! مقبول")
        else:
            print("💪 Need more work! حاول تاني - شد حيلك")
            
    except:
        print("❌ Please enter a valid number!")

# شغل البرنامج
check_grade()
