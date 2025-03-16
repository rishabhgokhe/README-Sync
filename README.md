# Readme-Sync

A Python script to automate README updates across multiple repositories by dynamically inserting or updating content blocks.

# Table of Contents

  - [Features](#-features)
  - [How It Works](#-how-it-works)
  - [Setup Instructions](#️-setup-instructions)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Example Block Structure](#-example-block-structure)
  - [Notes](#-notes)
  - [About Me](#-about-me)
  - [Connect with Me](#-connect-with-me)

## 🚀 Features

- Automatically updates README files in specified repositories.
- Dynamically replaces specific content blocks using predefined markers.
- Supports multiple reusable Markdown blocks (e.g., `connect-with-me.md`, `license.md`).
- Detects changes before updating to avoid unnecessary commits.
- Generates meaningful commit messages with updated block names.

## ✏️ How It Works
1. Fetches the existing `README.md` from the target repositories.
2. Checks for predefined markers (`<!-- block-name-start.md --> ... <!-- block-name-end.md -->`).
3. Updates only the modified sections while keeping the rest of the README unchanged.
4. Commits and pushes changes with a message like:
   ```
   Updated README: connect-with-me.md, license.md
   ```

## 📂 Example Block Structure
Inside your repo, store reusable Markdown files:
```
📂 readme-sync
 ┣ 📜 sync_readme.py
 ┣ 📜 connect-with-me.md
 ┣ 📜 contribution-guidlines.md
 ┣ 📜 license.md
 ┗ 📜 README.md
```

Each block should have start and end markers in the README:
```markdown
<!-- connect-with-me.md-start -->
[Your social links here]
<!-- connect-with-me.md-end -->
```

## 📌 Notes
- The script **only updates modified blocks** to prevent unnecessary commits.
- If no changes are detected, it skips the update process.
- Supports multiple repositories.

<!-- about-me.md-start -->
## 🚀 About Me
<!-- about-me.md-end -->

<!-- connect-with-me.md-start -->
## 🚀 Connect With Me
<!-- connect-with-me.md-end -->


## 🤝 Contributing
Pull requests are welcome! If you find issues or have suggestions, feel free to open an **Issue**.

## 📜 License
This project is licensed under the **MIT License**.

---

🚀 **Keep your README in sync effortlessly!** 🔄  