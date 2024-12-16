# Copy Blog Post Content

This project provides a suite of scripts to handle blog post content from an API. The scripts can fetch, save, and convert blog content, making it easy to manage blog posts in various formats like .docx, .csv, and .html.

## Features

1. Save blog content as .docx files with file names based on the blog post ID.
2. Extract and save blog metadata (ID, title, meta title, meta description, and file name) into a CSV file.
3. Save all blog posts as .docx files in one go.
4. Convert a specified .docx file to an .html format in text file.

---

## Scripts

### 1. Save Blog Content as `.docx` by ID

**Script Name**: `save_by_id.py`  
**Description**: Fetch a blog post by its ID from the API and save the content as a `.docx` file.

### Usage

```bash
python save_by_id.py
```

- Input: Blog post ID (provided during script execution).
- Output: .docx file (e.g., 9.docx) containing the blog post content.

---

### Save Blog Metadata to a CSV File

**Script Name**: `save_metadata_to_csv.py`.  
**Description:** Fetch metadata for all blog posts from the API and save it to a CSV file. The metadata includes:

- Blog Post ID
- Title
- Meta Title
- Meta Description
- File Name

---

### Save Blog Metadata to a CSV File

**Script Name**: `save_metadata_to_csv.py`.  
**Description:** Fetch metadata for all blog posts from the API and save it to a CSV file. The metadata includes:

```bash
python save_metadata_to_csv.py
```

- Blog Post ID
- Title
- Meta Title
- Meta Description
- File Name

---

### Save All Blog Posts as .docx Files

**Script Name:** save_all_posts.py  
**Description:** Fetch all blog posts from the API and save each post as a .docx file. The files are named after the blog post IDs (e.g., 9.docx, 10.docx).

```bash
python save_all_posts.py
```

**Output:** .docx files for all blog posts.

---

### Convert .docx File to .html

**Script Name:** convert_docx_to_html.py  
**Description:** Convert a .docx file to an .html file by providing the file name.

```bash
python convert_docx_to_html.py
```

**Input:** Name of the .docx file (e.g., 9.docx).  
**Output:** .text file with the same content as the .docx file.

---

### Dependencies

Run the following command to install all dependencies listed in the file:

```bash
pip install -r requirements.txt
```

### or

```bash
pip install mammoth requests beautifulsoup4 python-docx
```

## Configuration

Update the API URL and other parameters in a configuration file (e.g., config.json) to match your requirements.

# Personal Project

This script was developed as part of a personal project. Its primary purpose is to streamline the management and processing of blog content through various automation tasks, including fetching blog posts from an API, saving content to `.docx` and `.csv` formats, and converting files to `.txt`.

It is intended for personal use only and is not designed for commercial distribution.
