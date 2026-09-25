# Documents / OCR — Discovery Capture

Status: DISCOVERY_CAPTURED
Captured: 2026-09-25

## Sources

### OCRmyPDF
https://github.com/ocrmypdf/OCRmyPDF
- Adds an OCR text layer to scanned PDFs.
- Supports searchable PDF/A output, deskew/rotation, multiprocessing, image preservation and multilingual Tesseract OCR.
- MPL-2.0 core license; other components can have separate licenses.
- Strong candidate for local/private document processing because the repository explicitly emphasizes keeping private data private. citeturn0search3

### Docling
https://github.com/docling-project/docling
- Candidate local document-understanding/conversion stack.
- Preserve for recursive verification of supported formats, OCR/layout capabilities, model dependencies, licenses and hardware requirements.

### Tesseract
https://github.com/tesseract-ocr/tesseract
- Mature local OCR engine.
- Preserve as a foundational dependency for OCR pipelines and language coverage.

## Reusable patterns
- Local OCR before cloud document APIs
- PDF/A archival output
- Preserve original image resolution where possible
- Multilingual OCR
- Parallel page processing
- Validation of generated documents
- Separate OCR engine from document orchestration layer

## Verification rule
Discovery capture only. License, model weights, external runtime requirements, language quality and deployment cost must be verified before declaring a paid-service replacement.
