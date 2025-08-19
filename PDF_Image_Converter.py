import os
import img2pdf
from pdf2image import convert_from_path
from datetime import datetime

def images_to_pdf():
    print("\n=== Images to PDF Converter ===")
    images = []
    valid_ext = (".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif")

    # Collect multiple images
    while True:
        img_path = input("\nEnter the image path: ").strip()
        
        # ✅ Validate input image
        if not os.path.exists(img_path):
            print("❌ Error: Path does not exist. Try again.")
            continue
        if not os.path.isfile(img_path):
            print("❌ Error: This is a folder, not a file. Try again.")
            continue
        if not img_path.lower().endswith(valid_ext):
            print(f"❌ Error: Invalid file type. Allowed: {', '.join(valid_ext)}")
            continue
        
        images.append(img_path)
        print("✅ Image added successfully!")

        choice = input("\nDo you want to add another image? (y/n): ").strip().lower()
        if choice != "y":
            break

    # ✅ Ask for output path with strict validation
    while True:
        pdf_path = input("Enter full path to save the PDF (e.g., H:\\Documents\\output.pdf): ").strip()
        
        # Must end with .pdf
        if not pdf_path.lower().endswith(".pdf"):
            print("❌ Error: Output file must end with '.pdf'. Try again.")
            continue

        # Get folder path
        folder = os.path.dirname(pdf_path)
        if not folder:
            folder = os.getcwd()  # If user only gave filename, use current directory

        # Check if folder exists
        if not os.path.exists(folder):
            print("❌ Error: The folder does not exist. Please try again.")
            continue

        # If it's a folder, reject
        if os.path.isdir(pdf_path):
            print("❌ Error: You entered a folder. Please provide a filename ending with '.pdf'.")
            continue

        # If file already exists, confirm overwrite
        if os.path.exists(pdf_path):
            choice = input(f"⚠ File '{pdf_path}' already exists. Do you want to overwrite? (y/n): ").strip().lower()
            if choice == "y":
                break
            else:
                print("➡ Please enter a new file name or path.")
                continue
        else:
            break

    # ✅ Convert images to PDF
    with open(pdf_path, "wb") as f:
        f.write(img2pdf.convert(images))
    
    print(f"✅ Successfully created PDF at: {pdf_path}")


def pdf_to_images():
    print("\n=== PDF to Images Converter ===")

    # Ask for input PDF path
    while True:
        pdf_path = input("Enter the PDF path: ").strip()

        if not os.path.exists(pdf_path):
            print("❌ Error: Path does not exist. Try again.")
            continue
        if not os.path.isfile(pdf_path):
            print("❌ Error: This is a folder, not a file. Try again.")
            continue
        if not pdf_path.lower().endswith(".pdf"):
            print("❌ Error: Input file must be a PDF. Try again.")
            continue
        break

    # Ask for output folder
    while True:
        out_folder = input("Enter folder to save images (e.g., H:\\Documents\\Images): ").strip()

        if not os.path.exists(out_folder):
            print("❌ Error: The folder does not exist. Try again.")
            continue
        if not os.path.isdir(out_folder):
            print("❌ Error: Must be a folder path. Try again.")
            continue
        break

    # Convert PDF → Images
    try:
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]  # filename without extension
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        pages = convert_from_path(pdf_path, dpi=200)
        for i, page in enumerate(pages, start=1):
            out_file = os.path.join(out_folder, f"{pdf_name}_page_{i}_{timestamp}.jpg")
            page.save(out_file, "JPEG")
            print(f"✅ Saved: {out_file}")

        print("\n✅ PDF successfully converted into images!")
    except Exception as e:
        print(f"❌ Error during conversion: {e}")


def main():
    print("This is a PDF - Image Converter Program")
    while True:
        
        print("\n1. Convert Images to PDF")
        print("2. Convert PDF to Images")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            images_to_pdf()
        elif choice == "2":
            pdf_to_images()
        elif choice == "3":
            print("👋 Exiting... Have a nice day!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
