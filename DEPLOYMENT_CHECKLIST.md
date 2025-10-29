# Deployment Checklist for Render

## ✅ Phase 1: Code Preparation (COMPLETED)

- [x] Created `requirements.txt` with all dependencies
- [x] Modified `app.py` for production (environment variables, proper host/port)
- [x] Updated `index.html` with dynamic URLs
- [x] Created `.gitignore` file
- [x] Created `render.yaml` configuration
- [x] Added sample document to `data/` folder
- [x] Created `README.md` with instructions
- [x] Created `.env.example` template

## 📋 Phase 2: GitHub Setup

### Before You Start
- [ ] Have your GitHub account ready
- [ ] Have your repository URL ready

### Steps

1. **Copy All Files to Your Local Project**
   - [ ] Download all files from the outputs folder
   - [ ] Place them in your local project directory
   - [ ] Ensure the `data/` folder with `smartwatch-manual.pdf` is included

2. **Initialize Git (if not already done)**
   ```bash
   git init
   git add .
   git commit -m "Prepare for Render deployment"
   ```

3. **Push to GitHub**
   ```bash
   git remote add origin <your-github-repo-url>
   git branch -M main
   git push -u origin main
   ```

4. **Verify on GitHub**
   - [ ] Check that all files are visible on GitHub
   - [ ] Confirm `data/smartwatch-manual.pdf` is uploaded
   - [ ] Verify `.gitignore` is working (no `.env` file visible)

## 🚀 Phase 3: Render Deployment

### Before You Start
- [ ] Have your OpenAI API key ready
- [ ] Create a Render account at https://render.com

### Steps

1. **Create New Web Service**
   - [ ] Log into Render
   - [ ] Click "New +" → "Web Service"
   - [ ] Select "Connect GitHub" (authorize if first time)
   - [ ] Choose your repository

2. **Configure Service**
   
   Render should auto-detect settings from `render.yaml`, but verify:
   
   - **Name**: `rag-chatbot` (or your preferred name)
   - **Region**: Oregon (or closest to you)
   - **Branch**: `main`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python app.py`
   - **Plan**: Free

3. **Set Environment Variables**
   - [ ] Go to "Environment" tab
   - [ ] Click "Add Environment Variable"
   - [ ] Key: `OPENAI_API_KEY`
   - [ ] Value: (paste your OpenAI API key)
   - [ ] Click "Save Changes"

4. **Deploy**
   - [ ] Click "Create Web Service"
   - [ ] Wait 5-10 minutes for initial deployment
   - [ ] Watch the deployment logs for any errors

5. **Verify Deployment**
   - [ ] Once deployed, click the service URL (e.g., https://rag-chatbot-xxxx.onrender.com)
   - [ ] Check that the page loads
   - [ ] Try asking a question about the smartwatch
   - [ ] Test the upload functionality

## 🧪 Phase 4: Testing

### Test Cases

1. **Basic Functionality**
   - [ ] Page loads without errors
   - [ ] Can see the chat interface
   - [ ] Welcome message appears

2. **Sample Document Query**
   - [ ] Ask: "What's in the box with the TechFlow SmartWatch?"
   - [ ] Ask: "How long does the battery last?"
   - [ ] Ask: "What is the water resistance rating?"
   - [ ] Verify answers are accurate and from the document

3. **Upload Functionality**
   - [ ] Upload a new document
   - [ ] Verify success message
   - [ ] Ask a question about the new document
   - [ ] Verify the answer is relevant

4. **Error Handling**
   - [ ] Try sending empty message (should not send)
   - [ ] Try uploading invalid file type (should show error)

## 📝 Important Reminders

### Free Tier Limitations
- ⚠️ Service spins down after 15 minutes of inactivity
- ⚠️ First request after spin-down takes 30-60 seconds
- ⚠️ Uploaded files are lost on restart (sample document persists)
- ⚠️ 750 hours/month of runtime (sufficient for demo)

### If Something Goes Wrong

**Build Fails:**
- Check Render logs for specific error
- Verify `requirements.txt` is correct
- Ensure Python version is compatible

**App Crashes:**
- Check if OpenAI API key is set correctly
- Verify environment variables in Render dashboard
- Check application logs in Render

**Can't Query Documents:**
- Verify OpenAI API key has credits
- Check that `data/` folder contains documents
- Look for errors in Render logs

## 🎉 Success Criteria

Your deployment is successful when:
- [✓] App loads at your Render URL
- [✓] Can ask questions about the smartwatch manual
- [✓] Can upload new documents
- [✓] Receives relevant answers to queries

## 📞 Getting Help

If you encounter issues:
1. Check Render logs (Dashboard → Logs tab)
2. Verify environment variables are set
3. Test OpenAI API key separately
4. Review GitHub repo for missing files

## Next Steps After Deployment

- [ ] Share the URL with stakeholders
- [ ] Consider upgrading to paid tier for persistence
- [ ] Add more sample documents
- [ ] Customize the UI/branding
- [ ] Monitor usage and costs

---

**Your Render URL will be:** `https://<your-service-name>.onrender.com`

Good luck with your deployment! 🚀
