
def add_entry_to_html(file_path):
    # Read the current content of the HTML file
    with open(file_path, "r") as file:
        html_content = file.read()

    # Request user inputs
    date = input("Enter the date (e.g., Jeudi 2 Novembre 2023): ")
    time = input("Enter the time (e.g., 14h00): ")
    book_title = input("Enter the book title: ")
    author = input("Enter the author's name: ")
    book_image_file_name = input("Enter the book image file name (e.g., mybook-cover.jpg): ")
    brunch_image_file_name = input("Enter the brunch image file name (e.g., brunch-image.jpg): ")
    brunch_image_text = input("Enter the text for the brunch image hyperlink: ")
    summary = input("Enter the summary: ")

    # Append the brunch hyperlink to the summary
    summary += f' <a href="img/{brunch_image_file_name}" data-lightbox="image-1">{brunch_image_text}</a>.'

    # Create the new entry (without hyperlinks around the covers)
    new_entry = f'''
    <li>
        <span><img src="covers/{book_image_file_name}" alt="{book_image_file_name}" class="book-cover"></span>
        <i>{book_title}</i> — {author} <br>
        {date} à {time}
        <div class="synth-text"> <b>Summary :</b> {summary} </div>
    </li>
    '''

    # Insert the new entry at the top of the list
    insertion_point = html_content.find('<ol reversed class="img">') + len('<ol reversed class="img">')
    updated_html_content = html_content[:insertion_point] + new_entry + html_content[insertion_point:]

    # Save the updated content back to the HTML file
    with open(file_path, "w") as file:
        file.write(updated_html_content)

    print("Entry added successfully!")

# Run the function
if __name__ == "__main__":
    file_path = "index.html"  # Modify this path if needed
    add_entry_to_html(file_path)
