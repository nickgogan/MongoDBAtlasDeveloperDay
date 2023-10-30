# MongoDB Atlas Developer Day Workshop
**Last Updated:** October 30th, 2023
**Owner:** [Nick Gogan](nick.gogan@mongodb.com) (feel free to reach out!)

This hands-on workshop is meant to introduce developers new to MongoDB and MongoDB Atlas to how the database works. It was originally designed to be delivered in-person at a company's corporate office, using slides to facilitate the discussion before each exercise. Both physical and virtual attendees are expected to join a conference call to easily see this content.

Ideally, the workshop participants have already seen a MongoDB Atlas 101 presentation to get introduced to the core concepts of the platform in theory before doing this practice.

## Table of Contents
- Preparation
  - [Prerequisites](#prerequisites)
  - [Workshop Facilitator Checklist / Limitations to be Aware Of](#workshop-facilitator-checklist--limitations-to-be-aware-of)
  - [Troubleshooting Common Issues](#troubleshooting-common-issues)
- Execution: Choose one of the following approaches to the exercises:
  - [MongoDB Compass](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/tree/main/compass)
  - [Jupyter](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/tree/main/jupyter)
- Optional
  - [Get your own clean wikipedia dataset](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/tree/main/data)

## Prerequisites

1. **Create a [MongoDB Atlas Account](https://www.mongodb.com/docs/atlas/)** using your corporate email via [the registration page](https://www.mongodb.com/cloud/atlas/register). This account is used **only for logging into the Atlas control plane/web UI, not for the actual database.** This flow will create your initial [Atlas Organization](https://www.mongodb.com/docs/atlas/access/orgs-create-view-edit-delete/) and [Project](https://www.mongodb.com/docs/atlas/tutorial/manage-projects/), i.e. the containers for your database clusters. 
   - **Note**: If your corporate email is already associated with an Atlas Organization and you do not have the ability to create new free-tier Atlas clusters, then please contact your local MongoDB account team for options.

2. **Verify your account** via the emailed link. You will be redirected to an initial account setup experience.

3. **Deploy a database.** On the "Deploy Your Database" page:
   - Select the **M0** (i.e. free/shared-tier) option.
   - Scroll down and select your preferred cloud provider & region. The closer the selected region matches the geographical location of the workshop participants, the better.
   - Name your cluster (it will appear in your connection string later one) and, optionally, tag it with tags such as "DevDay workshop".
   - Hit the "Create" button at the bottom of the page. 

4. **Create your first database user.** You will be directed to the **Security Quickstart** flow to create your first db user. It is these credentials that will be used to actually authenticate to your data-bearing cluster via the connection string when doing the workshop exercises:
   - Choose "Username and Password" and fill the fields. 
   - Select "Create User".

5. **Add your IP address**: For those doing this at home and planning to do the workshop from the office, you will likely need to do this step again 
   - Scroll down and keep the default "My Local Environment".
   - Hit "Add My Current IP Address" to your current IP address to the IP Access List of your Atlas Project. 
   - Scroll down to the bottom of the page and hit "Finish and Close".

6. You will be presented with a small pop - select "Go to Overview" to see your M0 cluster being provisioned from your chosen cloud provider, in your selected region. Depending on the cloud provider and region, this can take anywhere from 10-20min. 

7. **Your are aready for the workshop!**

## Workshop Facilitator Checklist / Limitations to be Aware Of
1. **Visit the conference room in-person**: Ensure 
2. **Networking**: If doing the workshop at a company's site, be cognizant of any networking configuration (e.g. corporate firewall/VPN) that may block access to Atlas via Compass/Jupyter/web UI/etc. **Visit the office yourself and have 1+ participants that are typically onsite join a zoom with you and run through all of the workshop exercises to ensure a smooth flow.**
    - **Corporate WiFi vs Guest network**: Guest network typically has fewer restrictions, but are not ideal. Work with the company's IT & Security team to ensure access via the Corporate WiFi/VPN/Firewall.
    - **IP Address access**: If participants completed the setup work at home and are attending in-person, they will have a new IP address to add to their Atlas Project's IP Access List. See [Trobuleshooting/Add IP Address to Access List]()
- Sponsorship: If possible, first gather the emails of all registrants and identify those who already have their corporate emails associated with an existing Atlas Organization. 
  - Ask to introduce the workshop
- Ensure that participants have received the invite and prerequisites via email, slack, calendar invite, etc. 
  
1. **Conferencing**: If the workshop will be streamed via Zoom/Teams/etc., then:
   - Ask to be the Zoom host: Not being the host can lead to bottlenecks in allowing participants to join the call. 
   - Ensure Chat functionality: Do this for the facilitator and helpers to be able to properly assist attendees in a timely manner.

2. **Create teams**: Workshops seem to be more effective and fun when participants work in teams. 

3. **Bring enough support**: Ensure a ratio of roughly 1 helper/10 attendees.

## Troubleshooting Common Issues
1. **Corporate email already in use**: If an Atlas 
2. **Add IP Address to Access List**: MongoDB Atlas clusters only allow connections from known IP addresses. These addresses may change for a variety of reasons, from corporate IT policy rolling them on a regular basis to working on different networks (e.g. home vs corporate network/VPN). To add a new IP address to your Project's Access List via the [Atlas web GUI](https://cloud.mongodb.com/account/login):
    - Log in.
    - Go to "Network Access" on the left-hand panel.
    - Hit the "Add IP Address" button.
    - Add your current IP Address (there should be button to easily do this).
    - Optionally, add a comment to describe your IP address such as "Home" or "Office".
    - Optionally, make the entry temporary (6hrs to 1 week).
    - Allow a few moments for Atlas automation to make the change.
    - Try logging into your cluster using your db user (not your Atlas UI credentials).