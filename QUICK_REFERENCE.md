# 📝 Quick Reference Card - Aman's Job Pipeline Bot

## 🚀 Quick Start
```bash
# 1. Install Chrome from google.com/chrome
# 2. Install dependencies
pip install undetected-chromedriver pyautogui setuptools openai flask-cors flask selenium

# 3. Run the bot
python runAiBot.py

# 4. View results (in separate terminal)
python app.py
# Open: http://localhost:5000
```

---

## 👤 Your Profile
- **Name:** Aman Kumar
- **Email:** amankumar80451@gmail.com
- **LinkedIn Location:** India
- **Current CTC:** ₹12 LPA → **Expected:** ₹20 LPA
- **Experience:** 2.5 years (Data Engineer)
- **Target Roles:** Data Scientist, AI Engineer, ML Engineer

---

## 📂 Important Files

| File | Purpose |
|------|---------|
| `runAiBot.py` | Main bot script - RUN THIS |
| `config/secrets.py` | LinkedIn credentials |
| `config/questions.py` | Your answers (salary, experience, etc.) |
| `config/search.py` | Job search terms & filters |
| `config/personals.py` | Your personal info |
| `config/settings.py` | Bot behavior settings |
| `all resumes/default/resume.pdf` | Your resume ✅ Added |

---

## ⚙️ Key Settings

**`config/settings.py`**
```python
run_in_background = False      # True = silent, False = watch it work
click_gap = 1                  # Speed: 0=fast, 5=slow (human-like)
stealth_mode = True            # Avoid bot detection
pause_before_submit = True     # Review before applying
```

**`config/search.py`**
```python
search_terms = ["Data Scientist", "AI Engineer", ...]  # What to search
search_location = "India"       # Where to search
switch_number = 30              # Apps per search before switching
```

**`config/questions.py`**
```python
desired_salary = 2000000        # 20 LPA
current_ctc = 1200000           # 12 LPA
notice_period = 30              # Days
years_of_experience = "2.5"     # For forms
```

---

## 📊 Results

**Applications saved to:**
- ✅ `all excels/all_applied_applications_history.csv`
- ✅ `all excels/all_failed_applications_history.csv`
- ✅ `logs/` folder (detailed logs)

---

## 🛠️ Troubleshooting

| Problem | Solution |
|---------|----------|
| Chrome won't open | Install Chrome from google.com/chrome |
| Login fails | Check credentials in `config/secrets.py` |
| Resume not uploading | Verify path in `config/questions.py` |
| Bot encountering unknown questions | Set `pause_at_failed_question = True` |
| Bot too slow/fast | Adjust `click_gap` in `config/settings.py` |

---

## 📈 Expected Results

- **Speed:** 30-50 applications per hour
- **Success Rate:** ~60-70% depending on match
- **Time Saved:** ~2-3 minutes per application vs manual
- **Daily Limit:** ~100-150 applications (LinkedIn limit)

---

## 🎯 Workflow

```
1. Download repo to your PC
2. Install Chrome browser
3. pip install dependencies
4. Copy config files (already configured!)
5. python runAiBot.py
6. Watch the magic happen! ✨
7. Check results in CSV or web UI
```

---

## 📞 Support
- **GitHub:** github.com/GodsScion/Auto_job_applier_linkedIn
- **Discord:** discord.gg/fFp7uUzWCY

---

**Status:** ✅ Ready to Deploy  
**Date:** March 27, 2026  
**User:** Aman Kumar
