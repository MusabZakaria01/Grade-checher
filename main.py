# Grade Checker - My First Python Project
# Created by Musab - 2026


# 🎓 Grade Checker - معد الدرجات

أول مشروع بايثون لي - by MusabZakaria01

### ▶️ جرب المشروع مباشرة:
اضغط هنا وشغل الكود:
**[https://www.programiz.com/python-programming/online-compiler/](https://www.programiz.com/python-programming/online-compiler/)**

1. انسخ الكود من ملف `main.py`
2. الصقه في الموقع
3. اضغط Run وادخل درجتك!

### الفكرة
برنامج بسيط يحسب التقدير من الدرجة (ممتاز، جيد جدا، إلخ)

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
