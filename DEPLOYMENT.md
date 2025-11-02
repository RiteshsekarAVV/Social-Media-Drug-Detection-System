# Deployment Guide

This guide covers deploying your Flask Drug Detection application to various platforms.

## Prerequisites

1. **GitHub Account** - For code hosting
2. **Git installed** on your computer
3. **Project pushed to GitHub** repository

## Platform Options

### 🚀 Option 1: Render (Recommended - Easiest for Flask)

**Best for:** Flask apps, free tier available, easy setup

#### Steps:

1. **Push to GitHub:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Sign up/login with GitHub
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Settings:
     - **Name:** drug-detection-app
     - **Environment:** Python 3
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `python app.py`
   - Click "Create Web Service"
   - Your app will be live at: `https://drug-detection-app.onrender.com`

**Free Tier:** Includes 512 MB RAM, auto-sleeps after 15 min inactivity

---

### 🚂 Option 2: Railway (Recommended - Always On)

**Best for:** Always-on free tier, simple deployment

#### Steps:

1. **Push code to GitHub** (same as above)

2. **Deploy on Railway:**
   - Go to [railway.app](https://railway.app)
   - Sign up/login with GitHub
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway auto-detects Python and deploys
   - Get your URL: `https://your-app.up.railway.app`

**Free Tier:** $5 credit/month, always-on available

---

### ☁️ Option 3: Vercel (Serverless - Advanced)

**Best for:** Serverless architecture, edge functions

#### Steps:

1. **Install Vercel CLI:**
   ```bash
   npm i -g vercel
   ```

2. **Deploy:**
   ```bash
   vercel
   ```
   - Follow prompts
   - Your app will be at: `https://your-app.vercel.app`

**Note:** Vercel is serverless, so file storage (`reports/`) is ephemeral. PDFs won't persist.

---

### 🌐 Option 4: Cloudflare Workers/Pages

**Best for:** Edge computing, but requires modifications

#### Steps:

1. **Use Cloudflare Pages (Limited):**
   - Go to [Cloudflare Dashboard](https://dash.cloudflare.com)
   - Workers & Pages → Create Application
   - Connect GitHub repo
   - Build settings: `Python 3.11`
   - Output directory: `/`

**Note:** Flask apps work better on platforms designed for Python. Cloudflare is better for static sites or Workers (requires code changes).

---

### 🐍 Option 5: PythonAnywhere (Free Python Hosting)

**Best for:** Python-specific, free tier available

#### Steps:

1. **Create account:** [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload files:**
   - Go to Files tab
   - Upload `app.py`, `requirements.txt`, and `templates/` folder

3. **Configure Web App:**
   - Go to Web tab
   - Click "Add a new web app"
   - Select Flask → Python 3.10
   - Set source file: `/home/YOURUSERNAME/app.py`
   - Set working directory: `/home/YOURUSERNAME`

4. **Install dependencies:**
   - Go to Bash console
   - Run: `pip3.10 install --user flask fpdf2`

5. **Reload web app** → Your app is live!

**Free Tier:** `YOURUSERNAME.pythonanywhere.com`

---

## 🎯 Quick Comparison

| Platform | Free Tier | Flask Support | Setup Time | Always-On |
|---------|-----------|---------------|------------|-----------|
| **Render** | ✅ Yes | ⭐⭐⭐ Excellent | ⏱️ 5 min | ⚠️ Sleeps |
| **Railway** | ✅ $5 credit | ⭐⭐⭐ Excellent | ⏱️ 5 min | ✅ Yes |
| **PythonAnywhere** | ✅ Yes | ⭐⭐⭐ Excellent | ⏱️ 10 min | ✅ Yes |
| **Vercel** | ✅ Yes | ⭐⭐ Limited | ⏱️ 5 min | ✅ Yes |
| **Cloudflare** | ✅ Yes | ⭐ Limited | ⏱️ 15 min | ✅ Yes |

---

## 📝 Deployment Checklist

Before deploying, ensure:

- [ ] All files committed to Git
- [ ] `.gitignore` excludes `venv/`, `reports/`, `__pycache__/`
- [ ] `requirements.txt` is up to date
- [ ] `app.py` uses environment variables for port
- [ ] Tested locally

---

## 🔧 Environment Variables (Optional)

Some platforms allow you to set:

- `PORT` - Server port (auto-set by most platforms)
- `FLASK_ENV` - Set to `production` for production mode

---

## 🐛 Troubleshooting

### Issue: App crashes on deploy
**Solution:** Check build logs, ensure `requirements.txt` has all dependencies

### Issue: PDF generation fails
**Solution:** Ensure `reports/` directory has write permissions, or use temp storage

### Issue: Port already in use
**Solution:** Platform auto-assigns port, use `os.environ.get('PORT', 5000)` in code ✅ (Already done)

### Issue: Static files not loading
**Solution:** Ensure `templates/` folder is in root directory ✅ (Already done)

---

## 🚀 Recommended: Render or Railway

For fastest deployment:
1. **Render** - Best free tier for Flask
2. **Railway** - Best always-on option

Both support Flask natively and auto-detect Python apps!

