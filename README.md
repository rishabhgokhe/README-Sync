# Readme-Sync

A Python script to automate README updates across multiple repositories by dynamically inserting or updating content blocks.

# Table of Contents

  - [Features](#-features)
  - [How It Works](#-how-it-works)
  - [Example Block Structure](#-example-block-structure)
  - [Notes](#-notes)
  - [Code of Conduct](#-code-of-conduct)
  - [License](#-license)
  - [Contribution Guidelines](#-contribution-guidelines)
  - [Author](#-author)
  - [About Me](#-about-me)
  - [Feedback](#-feedback)
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
 ┣ 📜 generate_readmes.py
 ┣ 📜 connect-with-me.md
 ┣ 📜 contribution-guidelines.md
 ┣ 📜 license.md
 ┗ 📜 README.md
```

Each block should have start and end markers in the README:
```markdown
<!-- readme-file-name.md-start -->
Your Block Code Here
<!-- readme-file-name.md-end -->
```

## 📌 Notes
- The script **only updates modified blocks** to prevent unnecessary commits.
- If no changes are detected, it skips the update process.
- Supports multiple repositories.

## 📜 Code of Conduct

We expect all participants in our community to adhere to our Code of Conduct. Please read the full text [here](CODE_OF_CONDUCT.md).

## 🔒 License

This project is licensed under the **MIT License**.  
For full license details, refer to the **[LICENSE](LICENSE)** file.  

For any inquiries, please contact: 📧 [rishabhgokhe20contact@gmail.com](mailto:rishabhgokhe20contact@gmail.com)

<!-- contribution-guidelines.md-start -->
## 💡 Contribution Guidelines

Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add some feature'`).
5. Push to the branch (`git push origin feature/your-feature`).
6. Create a new Pull Request.
<!-- contribution-guidelines.md-end -->

<!-- author.md-start -->
## 👨🏻‍💻 Author

**Rishabh Gokhe**

![Open Source](https://img.shields.io/badge/Open%20Source-Lover-ff69b4?style=flat) ![Build With ❤️](https://img.shields.io/badge/Built%20With-%E2%9D%A4-red?style=flat)
<!-- author.md-end -->

<!-- about-me.md-start -->
## 🚀 About Me

Hi there! I'm Rishabh Gokhe, a full-stack developer passionate about building scalable, real-time, and user-friendly applications. I focus on crafting seamless digital experiences using modern technologies like WebSockets, React, and Node.js.

I enjoy exploring new ideas, experimenting with emerging tech, and collaborating with like-minded developers. Whether it's web development, UI/UX design, or optimizing performance, I'm always excited to push boundaries and create impactful solutions.

### My Vision

I believe technology should be intuitive, efficient, and accessible. My goal is to develop applications that enhance communication, productivity, and user experience. From real-time interactions to automation, I strive to build solutions that make a difference.

Feel free to reach out—always open to discussions, collaborations, and learning from fellow developers! 🚀
<!-- about-me.md-end -->

<!-- feedback.md-start -->
## 📨 Feedback

Got feedback, suggestions, or ideas? Feel free to reach out! [![Email Me](https://img.shields.io/badge/Email-Me-black?style=flat&logo=gmail&logoColor=white)](mailto:rishabhgokhe20contact@gmail.com)
<!-- feedback.md-end -->

<!-- connect-with-me.md-start -->
## <img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExeWxuNTJlaTIwcWp6Mmx4ODl5dXgxbThqNnI5eWh3YmIwMnZhbWp5MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/7NgYelDPXmzbzxrKsj/giphy.gif" width=40px /> Connect with Me

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/rishabh-gokhe-22168b287)
[![Portfolio](https://img.shields.io/badge/Portfolio-000000?style=for-the-badge&logo=outline&logoColor=white)](https://portfolio-rishabhgokhe.vercel.app/)
[![LeetCode](https://img.shields.io/badge/LeetCode-FFA116?style=for-the-badge&logo=leetcode&logoColor=white)](https://leetcode.com/u/rishabh_gokhe/)
[![Email](https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:rishabhgokhe20contact@gmail.com)
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/rishabhgokhe)
[![Twitter](https://img.shields.io/badge/Twitter-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://twitter.com/rishabhgokhe)
[![Instagram](https://img.shields.io/badge/Instagram-DD2A7B?style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/rishabh_gokhe)

**Email Address** : [rishabhgokhe20contact@gmail.com](mailto:rishabhgokhe20contact@gmail.com)
<!-- connect-with-me.md-end -->

---

🚀 **Keep your README in sync effortlessly!** 🔄  