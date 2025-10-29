# Quick Start Guide 🚀

## You Have 10 Files Ready for Deployment!

### Download These Files:
1. ✅ app.py
2. ✅ index.html  
3. ✅ requirements.txt
4. ✅ render.yaml
5. ✅ .gitignore
6. ✅ .env.example
7. ✅ README.md
8. ✅ DEPLOYMENT_CHECKLIST.md
9. ✅ PHASE1_SUMMARY.md (this is optional, just for reference)
10. ✅ data/smartwatch-manual.pdf

## 3-Step Deployment Process

### Step 1: Push to GitHub (5 minutes)
```bash
# In your project directory with all the files
git add .
git commit -m "Deploy RAG chatbot to Render"
git push origin main
```

### Step 2: Deploy on Render (10 minutes)
1. Go to https://render.com → New Web Service
2. Connect your GitHub repo
3. Render auto-detects settings from `render.yaml`
4. Add environment variable: `OPENAI_API_KEY` = your_key
5. Click "Create Web Service"
6. Wait for deployment ☕

### Step 3: Test (2 minutes)
1. Open your Render URL
2. Ask: "What's the battery life?"
3. Try uploading a document
4. Celebrate! 🎉

## Important Commands

**Local Testing:**
```bash
pip install -r requirements.txt
python app.py
# Visit: http://localhost:5000
```

**Git Commands:**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

## Need Help?

📖 Read: `DEPLOYMENT_CHECKLIST.md` for detailed steps
📖 Read: `README.md` for full documentation
📖 Read: `PHASE1_SUMMARY.md` for what changed

## Your OpenAI API Key

**Local (testing):** Create `.env` file with:
```
OPENAI_API_KEY=sk-your-key-here
```

**Render (production):** Add in dashboard Environment tab:
- Key: `OPENAI_API_KEY`
- Value: `sk-your-key-here`

## Expected Result

Your app will be live at:
```
https://your-service-name.onrender.com
```

Users can:
- ✅ Ask questions about the smartwatch manual
- ✅ Upload new documents  
- ✅ Get AI-powered answers

## Common Issues

**"No module named 'flask'"**
- Run: `pip install -r requirements.txt`

**"OpenAI API key not found"**
- Check environment variable is set in Render dashboard

**"App not loading"**
- Wait 60 seconds (free tier spins down)
- Check Render logs for errors

---

**Total Time: ~20 minutes**
**Cost: Free (with Render free tier)**

Let's do this! 💪
