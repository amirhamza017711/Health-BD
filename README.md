# **Contributor Guidelines: Creating Pull Requests for Updating Documents**

Welcome, collaborators! This guide outlines the steps for creating a pull request (PR) to update documents in the **chatbot-knowledge** repository. Please follow these instructions carefully to ensure a smooth contribution process.

---

## **Step 1: Fork the Repository**
1. Navigate to the repository at [**chatbot-knowledge**](https://git.dghs.gov.bd/riaz.somc/chatbot-knowledge.git).
2. Click the **Fork** button in the top-right corner to create your own copy of the repository.

---

## **Step 2: Clone the Repository**
1. Copy the URL of your forked repository.
2. Run the following command in your terminal to clone it to your local machine:
   ```bash
   git clone <your-fork-url>
   ```
3. Navigate to the project directory:
   ```bash
   cd chatbot-knowledge
   ```

---

## **Step 3: Create a New Branch**
1. Always create a new branch for your updates to keep the `main` branch clean:
   ```bash
   git checkout -b update-documents
   ```
   Replace `update-documents` with a branch name relevant to your changes.

---

## **Step 4: Make Your Changes**
1. Open the repository in your preferred code editor.
2. Update the document files with your changes.
3. Save the files.
4. You may use online platform to convert Microsoft Word document (if you have done your editing in MS Word) to a markup README file. To do this visit [https://word2md.com](https://word2md.com/).

---

## **Step 5: Commit Your Changes**
1. Stage your changes:
   ```bash
   git add .
   ```
2. Commit your changes with a clear and concise message:
   ```bash
   git commit -m "Update SHR documentation with new API integration details"
   ```
    Replace `Update SHR documentation with new API integration details` with your commit name.
---

## **Step 6: Push Your Changes**
1. Push your changes to your forked repository:
   ```bash
   git push origin <branch-name>
   ```
   Replace `<branch-name>` with the name of your branch.

---

## **Step 7: Create a Pull Request**
1. Go to your forked repository on [https://git.dghs.gov.bd/riaz.somc/chatbot-knowledge.git](https://git.dghs.gov.bd/riaz.somc/chatbot-knowledge.git).
2. Click on the **Compare & pull request** button.
3. Ensure the base repository is set to the **original repository** (`https://git.dghs.gov.bd/riaz.somc/chatbot-knowledge.git`) and the base branch is **main**.
4. Add a descriptive title for your pull request, e.g., `Update: Added API details in SHR documentation`.
5. Write a detailed description of the changes you made.
6. Click **Create pull request**.

---

## **Step 8: Collaborate on the PR**
1. Monitor your PR for any comments or feedback from the repository maintainers.
2. Make any requested changes by editing the files locally and pushing the updates:
   ```bash
   git add .
   git commit -m "Address feedback on PR"
   git push origin <branch-name>
   ```

---

## **Step 9: Merge the Pull Request**
1. Once the maintainers approve your PR, they will merge it into the main branch.
2. Alternatively, if you have merge permissions, click **Merge pull request** and confirm.

---

## **Additional Notes**
- Ensure your changes adhere to the repository's contribution guidelines.
- Always pull the latest changes from the main branch before starting a new update:
  ```bash
  git pull upstream main
  ```
- Use clear, professional language in your commit messages and PR descriptions.

Thank you for contributing to the **chatbot-knowledge** repository! Your efforts make this project better for everyone. 🎉