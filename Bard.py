from bardapi import BardCookies
import datetime

"""

To begin, please access the website https://bard.google.com/. Following that, right-click on the webpage and choose the "Inspect" option from the context menu. Once the developer tools panel is open, navigate to the "Application" tab. Within this tab, you will find a section labeled "Cookies." Locate and copy the values corresponding to "__Secure-1PSID," "__Secure-1PSIDTS," and "__Secure-1PSIDCC." Lastly, paste these copied values into the appropriate locations as required.

"""

cookie_dict = {
    "__Secure-1PSID": "agjgSlKpCgelEyq2jxXK9dkjz-exRLgue1JZ8qM6U4-M9SpRs9PokUj64Xhsu9ZmxHsSag.",
    "__Secure-1PSIDTS": "sidts-CjEBSAxbGcYD3grMTYCj5RE3JHw-ffypgsgU08MtGCQ7-OHxbyMc-kQKMLqT7cKaMhiyEAA",
    "__Secure-1PSIDCC": "APoG2W-BoYlRGYJZyX34gyRTq0ECnGOsL4AGURGAll_AlJUvK58X4YKmF33Ft8MRB51Hx45Vvg"
}

bard = BardCookies(cookie_dict=cookie_dict)

while True:
    Query = input ("Enter Your Query :")
    Reply = bard.get_answer(Query)['content']
    print(Reply)