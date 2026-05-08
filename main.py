import telebot
import os
import threading
from flask import Flask

# ১. রেন্ডারের জন্য ফ্লাস্ক সেটআপ (ফ্রি হোস্টিংয়ের জন্য জরুরি)
app = Flask(__name__)

@app.route('/')
def home():
    return "Health-BD Bot is Live!"

def run_flask():
    # রেন্ডার থেকে পোর্ট নম্বর নেওয়া, না থাকলে ৮০০০ ব্যবহার করা
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)

# ২. আলাদা থ্রেডে ফ্লাস্ক সার্ভার চালু করা
threading.Thread(target=run_flask).start()

# --- আপনার বটের আসল কোড শুরু ---
BOT_TOKEN = "7993443657:AAG70xknlViwpbfQNDukUMTQUQLZDqJx7D4"
bot = telebot.TeleBot(BOT_TOKEN)

KNOWLEDGE_FILES = [
    "HID.md", "vaxEPI.md", "Telemedicine.md", "SHR.md", 
    "HRIS.md", "CRVS.md", "openmrs.md", "MIS.md", 
    "ICD11.md", "PrivacyPolicySHR.md", "eappointment.md"
]

def search_in_files(query):
    results = []
    query = query.lower()
    
    for filename in KNOWLEDGE_FILES:
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                if query in content.lower():
                    start_index = content.lower().find(query)
                    snippet = content[start_index:start_index+500]
                    results.append(f"📄 **উৎস:** {filename}\n---\n...{snippet}...")
    
    return results

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "🔥 আমীর ভাই, আপনার 'স্মার্ট স্বাস্থ্য বট' এখন সচল! 🔥\n\n"
                          "আপনি স্বাস্থ্য অধিদপ্তরের যেকোনো বিষয় লিখে সার্চ দিন।\n"
                          "যেমন: NID, Vaccine, Hospital, Health ID ইত্যাদি।")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    query = message.text
    bot.send_chat_action(message.chat.id, 'typing')
    
    found_data = search_in_files(query)
    
    if found_data:
        for info in found_data[:3]:
            # এখানে Markdown ব্যবহার করার সময় খেয়াল রাখবেন যেন সিম্বলগুলো ঠিক থাকে
            try:
                bot.send_message(message.chat.id, info, parse_mode="Markdown")
            except:
                bot.send_message(message.chat.id, info) # এরর হলে সাধারণ টেক্সট হিসেবে পাঠাবে
    else:
        bot.reply_to(message, "দুঃখিত আমীর ভাই, এই কিউওয়ার্ড দিয়ে কোনো তথ্য ফাইলগুলোতে পাওয়া যায়নি।")

print("🚀 বট চালু হয়েছে... আমীর ভাই, এখন টেস্ট করে দেখুন!")

# ৩. বটের পোলিং শুরু (ইন্টারাপশন এড়াতে infinity_polling ব্যবহার করা ভালো)
bot.infinity_polling()
