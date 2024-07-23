# My Social Media Project

I'm excited to share my social media site, built from scratch using the powerful Django backend framework, HTML, and CSS. This project served as an excellent learning experience after exploring the capabilities of Django.

**Tech Stack:**

* Python 3.7.4 (Solid foundation for web development)
* Django (Robust and scalable backend framework)
* HTML (Building the structure and content)
* CSS (Applying styles, enhanced with Bootstrap for responsiveness)
* JQuery (Enhancing interactivity, specifically for the navbar dropdown)

**Challenges and Learnings:**

* **Django Mastery:** Delved deep into Django's core concepts, workspace organization, and project management.
* **Tagging Expertise:** Integrated `django-taggit` for managing post categorization.
* **Accounts Onboarding:** Implemented a user signup process with robust validation to prevent:
    * **Duplicate Usernames:** Ensures unique usernames for seamless user identification.
    * **Duplicate Emails:** Maintains account integrity and prevents confusion.
* **Authentication and Authorization:** Built a secure system for user verification and access control to determine user permissions.
* **Login Requirement:** Mandatory login for specific actions promotes security and targeted interactions.
* **Following System:** Established a mechanism for users to follow each other and explore content of interest.
    * **Following Recommendations:** Incorporated an algorithm (optional for future implementation) to suggest relevant users to follow based on unfollowed users and shared interests. (Consider libraries like `gensim` for topic modeling)
    * **Self-Following Prevention:** Precludes users from following or unfollowing themselves, upholding system integrity.
* **Draft Posts:** Implemented a system for users to save drafts, allowing them to compose and refine posts at their convenience.
    * **Scheduled Publishing:** (Future feature) Add the ability to schedule posts for future publication, enabling advanced content planning.
* **Post Editing:** Granted users the ability to edit their own posts.
* **Post Ownership:** Implemented security measures to prevent users from editing posts created by others.

**How to Use**

1. Clone the repository.
2. Run: `pip install requirements.txt`
3. Run: `py manage.py runserver`
4. Go to: `http://127.0.0.1:8000/` in your browser.
5. Enjoy.

**Features (remaining) to add:**

1. P2P Chats
2. Group chats
3. Google, Outlook, Facebook direct API signup
4. Algo to suggest people based on other followers
5. Cool frontend
6. Merging similar topics
