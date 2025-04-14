# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'uasal_development_guide'
copyright = '2025, UASAL'
author = 'UASAL'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
# html_static_path = ['_static']
html_static_path = []
html_theme_options = {
    # --- IMPORTANT SETTINGS FOR REPOSITORY LINKS ---
    # Add the name of the GitHub organisation/user.
    'github_user': 'uasal',
    # Add the name of the Git repository.
    'github_repo': 'uasal_development_guide',
    # Which branch to link to? ('master' or 'main' is common)
    'github_version': 'main',
    # **Crucially, specify the path FROM the repository root TO the directory
    # containing your conf.py file.** It usually needs leading/trailing slashes.
    'conf_py_path': '/source/',
    # Set 'vcs_pageview_mode' to 'blob' or 'edit' to enable the link
    'vcs_pageview_mode': 'blob', # 'blob' shows the file view, 'edit' shows the edit view
    # 'display_github': True, # Deprecated in newer versions, use vcs_pageview_mode
}
    
_source_suffix = locals().get('source_suffix', '.rst') # Get source_suffix if defined

# --- SETTINGS FOR REPO LINK ---

# GitHub username or organization name
github_user = 'uasal'
# Repository name
github_repo = 'uasal_development_guide'
# Default branch name (CHECK THIS on GitHub: usually 'main' or 'master')
github_version = 'main'
# Path in the repository root where your documentation lives
# (Relative path from repo root to the directory containing conf.py)
# CHECK THIS: Use '/docs/' if conf.py is in a 'docs' folder at the root
# Use '/' if conf.py is directly in the repository root.
conf_py_path = '/source/'

html_context = {
    # Enable "Edit on GitHub" link:
    'display_github': True,
    # Provide GitHub details:
    'github_user': github_user,
    'github_repo': github_repo,
    'github_version': github_version,
    'conf_py_path': conf_py_path,
    # Set the source file suffix (for edit links)
    'source_suffix': _source_suffix,
}
