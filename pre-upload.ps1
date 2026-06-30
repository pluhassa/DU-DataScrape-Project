# pre-upload.ps1
# This script is executed before uploading the project to the repository.
$ErrorActionPreference = "Stop"

Write-Host "Pre-upload is being checked..."

# 1) Checking to ensure it can run on this version of python
python --version
if ($LASTEXITCODE -ne 0) {
    Write-Host "Python is not installed or not found in PATH. Please install Python before uploading."
    exit 1
}

# 2) Run pre-commit hooks
Write-Host "`n Running pre-commit hooks..."
pre-commit run --all-files
if ($LASTEXITCODE -ne 0) {
    Write-Host "Pre-commit hooks found issues. Please fix them before uploading."
    exit 1
}

# 3) Run Pylint
Write-Host "`n Running Pylint..."
pylint main.py
if ($LASTEXITCODE -ne 0) {
    Write-Host "Pylint found issues. Please fix them before uploading."
    exit 1
}

# 4) Run the parser
Write-Host "`n Running the parser in main.py..."
python main.py --log-level INFO --platform X --file-path "example.txt"
if ($LASTEXITCODE -ne 0) {
    Write-Host "Parser found issues. Please fix them before uploading."
    exit 1
}

# 5) Run the unit tests
Write-Host "`n Running unit tests..."
python -m unittest discover -s tests -p "tests_*.py" -v
if ($LASTEXITCODE -ne 0) {
    Write-Host "Unit tests found issues. Please fix them before uploading."
    exit 1
}

# Everything passed, print a success message
Write-Host "`nPre-upload checks completed successfully."
