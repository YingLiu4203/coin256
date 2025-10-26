# Contributing to Coin256

Thank you for your interest in contributing to the Coin256 book! This document provides guidelines and information for contributors.

## 🎯 Ways to Contribute

### Content Contributions
- **Fix errors**: Typos, grammar, technical inaccuracies
- **Improve clarity**: Rewrite confusing sections
- **Add examples**: Code samples, diagrams, illustrations
- **Expand content**: Add new sections or chapters
- **Translate**: Help make the book accessible in other languages

### Non-Content Contributions
- **Report issues**: Found an error? Let us know!
- **Suggest improvements**: Ideas for better organization or content
- **Review PRs**: Help review other contributors' work
- **Share feedback**: Tell us what works and what doesn't

## 📝 Contribution Process

### 1. Before You Start
- Check existing [Issues](../../issues) and [Pull Requests](../../pulls) to avoid duplication
- For major changes, open an issue first to discuss your ideas
- Review the book structure and existing content

### 2. Making Changes

#### Small Changes (typos, minor fixes)
- Can be made directly via GitHub's web interface
- Click "Edit" button on any file
- Make your changes and submit a pull request

#### Larger Changes
1. **Fork** the repository to your GitHub account
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/coin256-book.git
   cd coin256-book
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b descriptive-branch-name
   ```
4. **Make your changes** following our guidelines (see below)
5. **Commit** with clear messages:
   ```bash
   git add .
   git commit -m "Brief description of changes"
   ```
6. **Push** to your fork:
   ```bash
   git push origin descriptive-branch-name
   ```
7. **Open a Pull Request** from your fork to the main repository

### 3. Pull Request Guidelines

Your PR should:
- Have a clear title describing the change
- Include a description of what changed and why
- Reference any related issues (e.g., "Fixes #123")
- Be focused on a single topic or change
- Pass any automated checks

## ✍️ Content Guidelines

### Writing Style
- **Clear and accessible**: Write for a broad audience
- **Technically accurate**: Verify facts and examples
- **Consistent**: Match the style of existing content
- **Well-structured**: Use headers, lists, and formatting effectively

### Chapter Structure
Each chapter should follow this structure:
```
chapter-XX-name/
  ├── README.md          # Main chapter content
  ├── images/            # Screenshots, diagrams, illustrations
  └── examples/          # Code examples, demos, data files
```

### Markdown Formatting
- Use `#` for main chapter title (H1)
- Use `##` for major sections (H2)
- Use `###` for subsections (H3)
- Use code blocks with language specification:
  ````markdown
  ```python
  # Your code here
  ```
  ````
- Use tables for structured data
- Use lists for sequential or related items

### Adding Images
1. Place images in the chapter's `images/` folder
2. Use descriptive filenames: `hash-function-diagram.png`
3. Reference in markdown: `![Description](./images/filename.png)`
4. Optimize image size (prefer PNG for diagrams, JPG for photos)

### Code Examples
1. Place code files in the chapter's `examples/` folder
2. Include comments explaining the code
3. Test all code examples to ensure they work
4. Specify language and dependencies clearly

### Citations and References
- Link to authoritative sources
- Credit original authors and sources
- Prefer open-access or freely available resources

## 🔍 Review Process

1. **Automated checks**: May include linting, spell-check, or link validation
2. **Maintainer review**: A maintainer will review your contribution
3. **Feedback**: You may receive suggestions for improvements
4. **Approval**: Once approved, your PR will be merged

## 📜 License

By contributing to this project, you agree that your contributions will be licensed under the Apache License 2.0, the same license as the project.

## 🤝 Code of Conduct

### Our Pledge
We are committed to providing a welcoming and inclusive environment for all contributors.

### Expected Behavior
- Be respectful and considerate
- Welcome newcomers and help them learn
- Focus on constructive feedback
- Respect differing viewpoints and experiences

### Unacceptable Behavior
- Harassment, discrimination, or offensive comments
- Trolling or insulting remarks
- Publishing others' private information
- Any conduct inappropriate in a professional setting

## 💬 Getting Help

- **Questions?** Open an [issue](../../issues) with the "question" label
- **Discussion?** Use the [Discussions](../../discussions) tab
- **Stuck?** Don't hesitate to ask for help in your PR

## 🙏 Thank You!

Every contribution, no matter how small, helps make this book better. We appreciate your time and effort!

---

Happy contributing! 🚀
