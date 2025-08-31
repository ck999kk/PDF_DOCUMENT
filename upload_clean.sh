#!/bin/bash
set -euo pipefail

# ตั้งค่า Repo URL
REPO_URL="git@github.com:ck999kk/PDF_DOUCUMENT.git"

# ตรวจสอบว่ามีโฟลเดอร์ .git อยู่หรือยัง ถ้าไม่มีให้ clone ใหม่
if [ ! -d ".git" ]; then
  echo "Cloning fresh repo..."
  rm -rf .git
  git init
  git remote add origin "$REPO_URL"
else
  echo "Resetting existing repo..."
  git remote set-url origin "$REPO_URL"
fi

# ล้าง history เดิมทั้งหมด
git checkout --orphan temp_branch
git add -A
git commit -m "Clean upload on $(date -u +%Y-%m-%dT%H:%M:%SZ)"
git branch -D main || true
git branch -m main

# Force push แบบแทนที่ทุกอย่าง
git push -f origin main

echo "Upload complete: $REPO_URL"
