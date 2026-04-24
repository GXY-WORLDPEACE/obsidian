from pypdf import PdfReader
import os

lectures = [
    ("1.Introduction to the lecture.pdf", "1"),
    ("2.linear.pdf", "2"),
    ("3.intro2nn.pdf", "3"),
    ("4.optimization_and_backprop.pdf", "4"),
    ("5.scaling_optimization.pdf", "5"),
    ("6.trainingnn.pdf", "6"),
    ("7.losses_and_activations.pdf", "7"),
    ("8.augmentation_and_regularization.pdf", "8"),
    ("9.convnets.pdf", "9"),
    ("10.architectures.pdf", "10"),
    ("11.rnns_and_transformers.pdf", "11"),
    ("12.advanced_dl_topics.pdf", "12"),
]

base_path = "1_raw/articles/I2DL/lectures"
output_file = "lectures_extracted.txt"

with open(output_file, "w", encoding="utf-8") as out:
    for filename, num in lectures:
        filepath = os.path.join(base_path, filename)
        out.write(f"\n{'='*80}\n")
        out.write(f"LECTURE {num}: {filename}\n")
        out.write(f"{'='*80}\n\n")
        try:
            reader = PdfReader(filepath)
            for i, page in enumerate(reader.pages):
                text = page.extract_text() or ""
                out.write(f"--- Page {i+1} ---\n{text}\n")
        except Exception as e:
            out.write(f"Error reading: {e}\n")

print(f"Extracted to {output_file}")