import time
from markitdown import MarkItDown
start_time = time.time()  # Start timing
md = MarkItDown()
result = md.convert("/Users/vallabhsumanth/Desktop/MArkitdown/Markitdown/packages/2022 IT Budget (1).xlsx")
print(result.text_content)

output_file = "output.md"
with open(output_file, "w", encoding="utf-8") as file:
    file.write(result.text_content)

end_time = time.time()  # End timing

elapsed_time = end_time - start_time
print(f"Markdown content has been written to {output_file}")
print(f"Time taken is : {elapsed_time:.2f} seconds")


# from markitdown import MarkItDown

# md = MarkItDown(docintel_endpoint="<document_intelligence_endpoint>")
# result = md.convert("/Users/vallabhsumanth/Desktop/MArkitdown/Markitdown/packages/Kokoro Documentation,Step Fun.pdf")
# print(result.text_content)


# from markitdown import MarkItDown

# # Initialize MarkItDown without plugins
# md = MarkItDown(enable_plugins=False)

# # Path to your Excel file
# file_path = "/Users/vallabhsumanth/Desktop/MArkitdown/Markitdown/packages/2022 IT Budget (1).xlsx"

# # Convert the file
# result = md.convert(file_path)

# # Preview the text content in terminal
# print("Converted Text Content:\n")
# print(result.text_content)

# # Optional: Save the preview to a markdown file
# with open("converted_output.md", "w", encoding="utf-8") as f:
#     f.write(result.text_content)

# print("\nConversion complete. Output saved to 'converted_output.md'")
