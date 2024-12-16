import csv
import requests

def fetch_data(api_endpoint, token):
    headers = {
        'Authorization': f'Token {token}'
    }
    try:
        response = requests.get(api_endpoint, headers=headers)
        response.raise_for_status()  # Raises an exception for 4XX/5XX errors
        return response.json()
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
        return None

def save_to_csv(data, filename='output.csv'):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Write the header
        writer.writerow(['ID', 'Title', 'Meta Title', 'Meta Description', 'DOCX Filename'])
        # Write the data
        for item in data:
            id = item.get('id', '')
            title = item.get('title', '')
            meta_title = item.get('meta_title', '')
            meta_description = item.get('meta_description', '')
            docx_filename = f"{id}.docx" if id else ''
            writer.writerow([id, title, meta_title, meta_description, docx_filename])

def main():
    api_endpoint = "<SITE_NAME>/api/blogs/"
    token = "YOUR_API_TOKEN"  # Replace YOUR_API_TOKEN with your actual API token
    data = fetch_data(api_endpoint, token)
    if data is not None:
        save_to_csv(data)

if __name__ == "__main__":
    main()
