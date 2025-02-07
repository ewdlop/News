On GitHub, **secrets** are stored in **GitHub Actions Secrets** and **Dependabot Secrets**. These are encrypted and can be used in workflows securely.

---

## **🔹 How to Add a Secret in GitHub Actions**
### **Step 1: Navigate to Your Repository's Settings**
1. Go to **your repository** on GitHub.
2. Click on **"Settings"** (⚙️).
3. Scroll down and click on **"Secrets and variables" → "Actions"**.

---

### **Step 2: Add a New Secret**
1. Click **"New repository secret"**.
2. Enter the **name** of the secret (e.g., `GOOGLE_TRANSLATE_API_KEY`).
3. Paste the **secret value** (e.g., API key, password, or token).
4. Click **"Add secret"**.

---

## **🔹 How to Use Secrets in GitHub Actions**
Once stored, you can access them in your workflow using the **`${{ secrets.SECRET_NAME }}`** syntax.

### **Example Usage in a GitHub Action**
```yaml
jobs:
  example_job:
    runs-on: ubuntu-latest
    steps:
      - name: Access Secret
        run: echo "My secret is ${{ secrets.MY_SECRET }}" # Never echo secrets in real workflows!
```

**⚠️ Warning:** Never print secrets to the console (`echo`), as they can be exposed in logs.

---

## **🔹 Where Else Can You Store Secrets?**
- **Organization Secrets** (For all repositories in an organization)
- **Environment Secrets** (Scoped to specific environments like `staging`, `production`)
- **Dependabot Secrets** (For managing dependency updates)

---

### **Need to Secure API Keys in GitHub?**
- **Rotate secrets regularly**.
- **Use GitHub Environments** for different scopes (e.g., `dev`, `prod`).
- **Never hardcode secrets** in your repo.

Need help integrating secrets into a specific workflow? 🚀
