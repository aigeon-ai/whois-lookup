import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/Zozor54/api/whois-lookup'

mcp = FastMCP('whois-lookup')

@mcp.tool()
def whoisapi_real_time_domain_registration_details(domain: Annotated[str, Field(description='')],
                                                   format: Annotated[Union[str, None], Field(description='Choose your format : Json or Xml')] = None,
                                                   _forceRefresh: Annotated[Union[str, None], Field(description='Our data are cached for 3 days. If you only want real time data you can add this parameter in your request: _forceRefresh=1 to force a real time fetch but this would cost 2 times the credit.')] = None) -> dict: 
    '''Our WHOIS API provides accurate and real-time domain registration details in a standardized format, perfect for enhancing security assessments and monitoring domain status.'''
    url = 'https://zozor54-whois-lookup-v1.p.rapidapi.com/'
    headers = {'x-rapidapi-host': 'zozor54-whois-lookup-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'domain': domain,
        'format': format,
        '_forceRefresh': _forceRefresh,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def nslookup_api_comprehensive_dns_record_retrieval(domain: Annotated[str, Field(description='The domain name you want to look up.')]) -> dict: 
    '''NsLookup queries the specified DNS server and retrieves the requested records that are associated with the domain name you provided. These records contain information like the domain name’s IP addresses. The following types of DNS records are especially useful: - **A**: the IPv4 address of the domain. - **AAAA**: the domain’s IPv6 address. - **CNAME**: the canonical name — allowing one domain name to map on to another. This allows more than one website to refer to a single web server. - **MX**: the server that handles email for the domain. - **NS**: one or more authoritative name server records for the domain. - **TXT**: a record containing information for use outside the DNS server. The content takes the form name=value. This information is used for many things including authentication schemes such as SPF and DKIM.'''
    url = 'https://zozor54-whois-lookup-v1.p.rapidapi.com/nslookup'
    headers = {'x-rapidapi-host': 'zozor54-whois-lookup-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'domain': domain,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def sslcert_api_secure_certificate_insights(domain: Annotated[str, Field(description='')]) -> dict: 
    '''The SSL Certificates Information endpoint retrieves and validates the SSL certificate details for a specified domain, including issuer information, validity period, and current status. This endpoint helps ensure that the SSL certificate is correctly installed and up to date.'''
    url = 'https://zozor54-whois-lookup-v1.p.rapidapi.com/ssl-cert-check'
    headers = {'x-rapidapi-host': 'zozor54-whois-lookup-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'domain': domain,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def domain_information_from_ip(ip: Annotated[str, Field(description='')]) -> dict: 
    '''Get reverse Whois from Ip.'''
    url = 'https://zozor54-whois-lookup-v1.p.rapidapi.com/reverseWhois'
    headers = {'x-rapidapi-host': 'zozor54-whois-lookup-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'ip': ip,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def random_whois() -> dict: 
    '''Get 250 random whois from our database. All these whois are from registered domain.'''
    url = 'https://zozor54-whois-lookup-v1.p.rapidapi.com/randomWhois'
    headers = {'x-rapidapi-host': 'zozor54-whois-lookup-v1.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
