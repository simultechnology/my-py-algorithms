import httplib2


def check_google_accounts_access():
    url = 'https://accounts.google.com'
    system_cert_path = "/etc/ssl/cert.pem"
    http = httplib2.Http(ca_certs=system_cert_path)

    try:
        response, content = http.request(url, 'GET')
        print(f"Response status: {response.status}")
        print(f"Response content: {content[:100]}...")  # Contentの最初の100文字を表示
    except httplib2.HttpLib2Error as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    check_google_accounts_access()