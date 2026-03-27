# 🚀 LinkedIn Job Pipeline Bot - Setup & Configuration Guide

**Created:** March 27, 2026  
**User:** Aman Kumar  
**Status:** ✅ Ready to Deploy

---

## 📋 Your Profile Summary

### Personal Information
- **Name:** Aman Kumar
- **Email:** amankumar80451@gmail.com
- **Country:** India
- **Current Experience:** 2.5 years
- **Current Role:** Data Engineer
- **Education:** No Masters degree

### Salary & Employment Terms
- **Expected Salary:** ₹20,00,000 (20 LPA) 💰
- **Current CTC:** ₹12,00,000 (12 LPA)
- **Notice Period:** 30 days
- **Years of Experience:** 2.5 years

### Job Search Preferences
- **Target Roles:**
  - Data Scientist
  - AI Engineer
  - Machine Learning Engineer
  - Data Scientist - AI/ML
  - Artificial Intelligence Engineer
- **Location:** India
- **Jobs per Search:** 30 applications before switching to next role

### Resume
- **File:** `all resumes/default/resume.pdf`
- **Status:** ✅ Uploaded (aman_resume 9Mar.pdf)

### LinkedIn Credentials
- **Email:** amankumar80451@gmail.com
- **Password:** Stored in `config/secrets.py`

### Bot Settings
- **AI Mode:** ❌ DISABLED (Uses your personal resume)
- **Background Mode:** ✅ Can be toggled
- **Stealth Mode:** ✅ Enabled (Anti-bot detection)

---

## 🔧 Configuration Files Status

| File | Status | Details |
|------|--------|---------|
| `config/personals.py` | ✅ Configured | Your personal information |
| `config/questions.py` | ✅ Configured | Salary, experience, answers |
| `config/search.py` | ✅ Configured | Job search terms, location, filters |
| `config/secrets.py` | ✅ Configured | LinkedIn credentials |
| `config/settings.py` | ⚠️ Can Customize | Bot behavior (click speed, background, etc.) |
| `all resumes/default/resume.pdf` | ✅ Added | Your resume file |

---

## 🖥️ Installation Instructions

### Prerequisites
- **Python:** 3.10 or higher
- **Google Chrome:** Latest version
- **Operating System:** Windows, Mac, or Linux

### Step 1: Download the Repository

```bash
git clone https://github.com/Amank3110/job-pipeline.git
cd job-pipeline
```

### Step 2: Install Google Chrome

- **Windows/Mac:** https://www.google.com/chrome
- **Linux:** 
  ```bash
  sudo apt-get update
  sudo apt-get install google-chrome-stable
  ```

### Step 3: Install Python Dependencies

```bash
pip install undetected-chromedriver pyautogui setuptools openai flask-cors flask selenium
```

### Step 4: Copy Your Configuration Files

Copy these files from the codespace to your local repository:
- `config/personals.py`
- `config/questions.py`
- `config/search.py`
- `config/secrets.py`
- `all resumes/default/resume.pdf`

### Step 5: Verify LinkedIn Credentials

Open `config/secrets.py` and verify:
```python
username = "amankumar80451@gmail.com"
password = "Kashyap@31"
```

---

## 🚀 Running the Bot

### Quick Start
```bash
python runAiBot.py
```

### What the Bot Will Do
1. ✅ Open Google Chrome browser
2. ✅ Login to LinkedIn with your credentials
3. ✅ Search for Data Scientist & AI Engineer roles in India
4. ✅ Filter jobs based on your experience level
5. ✅ Apply to matching jobs with your resume
6. ✅ Auto-fill application forms with your pre-configured answers
7. ✅ Save all applications to CSV file: `all excels/all_applied_applications_history.csv`

### Monitor Progress
```bash
# In a separate terminal
python app.py
# Open browser: http://localhost:5000
```

---

## 📊 Application Results

The bot will create/update these files:

### `all excels/all_applied_applications_history.csv`
- Job ID
- Title
- Company
- HR Contact Information
- LinkedIn Job Link
- Date Applied
- Resume Used

### `all excels/all_failed_applications_history.csv`
- Failed applications with reasons
- For debugging and analysis

### `logs/` folder
- Detailed logs of bot activity

---

## ⚙️ Customization Options

### If You Want Different Settings

**In `config/settings.py`:**
- `run_in_background = True` → Bot runs silently
- `run_in_background = False` → You can see the bot working
- `click_gap = 0` → Fast clicking
- `click_gap = 5` → Slower, more human-like
- `stealth_mode = True` → Avoid LinkedIn bot detection

**In `config/search.py`:**
- `switch_number = 10` → Apply to 10 jobs per search term
- `switch_number = 50` → Apply to 50 jobs per search term

**In `config/questions.py`:**
- `pause_before_submit = True` → Review before each application
- `pause_at_failed_question = True` → Ask for help on unknown questions

---

## ❓ Troubleshooting

### Issue: Chrome Won't Open
**Solution:** 
- Ensure Google Chrome is installed in default location
- Check Chrome version matches ChromeDriver version

### Issue: LinkedIn Login Fails
**Solution:**
- Verify credentials in `config/secrets.py`
- Try manual login when prompted
- Check if 2FA is enabled on your account

### Issue: Resume Not Uploading
**Solution:**
- Verify file path in `config/questions.py`
- Check resume file exists at `all resumes/default/resume.pdf`
- Try a different PDF file format

### Issue: Forms Have Unknown Questions
**Solution:**
- Set `pause_at_failed_question = True` in `config/questions.py`
- Bot will ask you for answers to unknown questions

### Issue: Bot Too Fast/Slow
**Solution:**
- Adjust `click_gap` value in `config/settings.py`
- Higher value = slower (more human-like)

---

## 📞 Support Resources

- **GitHub Issues:** https://github.com/GodsScion/Auto_job_applier_linkedIn/issues
- **Discord Community:** https://discord.gg/fFp7uUzWCY
- **Original Repository:** https://github.com/GodsScion/Auto_job_applier_linkedIn

---

## ⚠️ Important Notes

1. **LinkedIn ToS:** This tool is for personal use. Use responsibly.
2. **Rate Limiting:** Bot sleeps 10 minutes between search cycles to avoid detection
3. **Daily Limits:** LinkedIn may have daily Easy Apply limits (~100-150 per day)
4. **First Run:** Allow extra time - bot will verify your configuration
5. **Resume Updates:** Update `all resumes/default/resume.pdf` if you change your resume

---

## 📈 Expected Performance

- **Applications per Hour:** ~30-50 (depending on form complexity)
- **Time Saved per Application:** ~2-3 minutes of manual work
- **Total Applications:** 100+ possible in 2-3 hours

---

## 🎯 Next Steps

1. ✅ Download this repository to your local machine
2. ✅ Ensure Google Chrome is installed
3. ✅ Copy your configuration files
4. ✅ Run: `python runAiBot.py`
5. ✅ Monitor results: View CSV files or web UI

---

**Last Updated:** March 27, 2026  
**Python Version Used:** 3.12.1  
**Status:** ✅ Ready for Production

Good luck with your job applications! 🚀💼
