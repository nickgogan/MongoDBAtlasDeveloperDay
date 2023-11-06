# MongoDB Atlas Developer Day Workshop
- **Last Updated:** October 30th, 2023
- **Owner:** [Nick Gogan](nick.gogan@mongodb.com) (feel free to reach out!)

This hands-on workshop is meant to introduce developers new to MongoDB and MongoDB Atlas to how the data platform works. It was originally designed to be delivered in-person at a company's corporate office, using slides to facilitate the discussion before each exercise. Both physical and virtual attendees are expected to join a conference call to easily see this content. The slide deck is internal to MongoDB and only accessible as a static PDF in this repo. Some of the slides are embedded GIFs that will look off when viewed as a PDF - that is normal & expected! Those slides demonstrate how to navigate an interface or input a specific command, both of which are available as plaintext in the README of whatever content delivery method you choose (Compass/Shell, Jupyter notebook, etc.). Note that any link in the slides should be clickable when the PDF is opened locally. 

Ideally, the workshop participants have already seen a MongoDB Atlas 101 presentation to get introduced to the core concepts of the platform in theory before doing this practice.

The exercises cover (via different content delivery mechanisms like [MongoDB Compass](https://www.mongodb.com/docs/compass/current/) and Jupyter notebooks):
- CRUD operations over [the Atlas sample dataset](https://www.mongodb.com/docs/atlas/sample-data/).
- Query analysis and indexes.
- Basic aggregations.
- Fulltext search using [Atlas Search](https://www.mongodb.com/docs/atlas/atlas-search/) and a sample wikipedia dataset.
- [Semantic search](https://www.mongodb.com/products/platform/atlas-vector-search) using the vectorized wikipedia dataset (same one)

## Table of Contents
- [MongoDB Atlas Developer Day Workshop](#mongodb-atlas-developer-day-workshop)
  - [Table of Contents](#table-of-contents)
  - [Sample Agenda](#sample-agenda)
    - [Full Day](#full-day)
    - [Half Day](#half-day)
  - [Attendee Prerequisites](#attendee-prerequisites)
  - [Workshop Facilitator Prerequisites](#workshop-facilitator-prerequisites)
  - [Troubleshooting Common Issues](#troubleshooting-common-issues)

## Sample Agenda
### Full Day
* 9:30 - 10:00 am: Arrivals and Breakfast (courtesy by MongoDB)

* 10:00 - 10:15 am: Welcome Remarks and Developer Day Kick Off

* 10:15 - 11:00 am: MongoDB Developer Data Platform Overview with MongoDB Solution Architects

* 11:00 - 12:30 pm: (Workshop) MongoDB Data Model and Query Fundamentals

* 12:30 - 1:30 pm: Lunch Break (courtesy of MongoDB)

* 1:30 - 3:00 pm: (Workshop) MongoDB Atlas Search and Vector Search

* 3:00 - 3:45 pm: Wrap up (Q/A, Use Case Discussions, etc.)

* 3:45 - 5:00 pm: Executive Engagement, Vision, and Roadmap with MongoDB Product Executive(s)

* 5:00 pm: Happy Hour! (courtesy of MongoDB)

### Half Day
>It's recommended that the audience had an initial MongoDB 101 presentation to be ready to do the Developer Day exercises. 

* 9:30 - 10:00 am: Arrivals and Breakfast (courtesy by MongoDB)

* 10:00 - 10:15 am: Welcome Remarks and Developer Day Kick Off

* 10:15 - 12:00 pm: (Workshop) MongoDB Data Model and Query Fundamentals

* 12:00 - 12:30 pm: Lunch Break (courtesy of MongoDB)

* 1:00 - 2:00 pm: (Workshop) MongoDB Atlas Search and Vector Search

## Attendee Prerequisites

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

## Workshop Facilitator Prerequisites
1. **Visit the conference room in-person**: Ensure that you have everything you need to deliver the content for both the in-person and virtual attendees. For example:
   -   If the room is large, you may need a microphone. 
   -   Ensure connectivity to the right onsite network.
   -   HDMI, accessories, etc. 

2. **Networking**: If doing the workshop at a company's site, be cognizant of any networking configuration (e.g. corporate firewall/VPN) that may block access to Atlas via Compass/Jupyter/web UI/etc. **Visit the office yourself and have 1+ participants that are typically onsite join a zoom/be in-person with you and run through all of the workshop exercises to ensure a smooth flow.**
    - **Corporate WiFi vs Guest network**: A guest network typically has fewer restrictions, but are not ideal in many cases. Work with the company's IT & Security team to ensure access via the Corporate WiFi/VPN/Firewall.
    - **IP Address access**: If participants completed the setup work at home and are attending in-person, they will have a new IP address to add to their Atlas Project's IP Access List. See [Trobuleshooting/Add IP Address to Access List](https://www.mongodb.com/docs/atlas/government/tutorial/allow-ip/).

3. **Conferencing**: If the workshop will be streamed via Zoom/Teams/etc., then:
   - **Ask to be the Zoom host**: Not being the host can lead to bottlenecks in allowing participants to join the call. 
   - **Ensure Chat functionality**: Do this for the facilitator and all helpers to be able to properly assist attendees in a timely manner.

3. **Gather the full participants list**: Gather the (corporate) emails of all registrants and identify those who already have their corporate emails associated with an existing Atlas Organization. 
    - **Ensure attendee prerequisites are shared**: All participants have received prerequisites, the calendar invite, etc. as soon as those are fully nailed down. It's important to have an idea of how many people will actually show up & participate, and the calendar invite tells you this.
    - **Ensure each attendee has their Atlas account**: For participants that are already part of an existing Atlas Organization via their corporate email address, find another way for them to provision their own free-tier/M0 cluster. This could be using a private/personal email address for just this workshop (include instructions to throw away the Atlas resources after the workshop is done) or using a single, dedicated Atlas cluster that is hosted by MongoDB for the workshop and which every attendee will use. 
      - For participants that are part of existing Atlas Organizations AND whose Projects have an existing free-tier/M0 cluster, reach out to either create a separate Organization or separate Project. This is because [Atlas Projects can only have 1 free-tier cluster](https://www.mongodb.com/docs/atlas/reference/free-shared-limitations/#operational-limitations).
    - **Designate teams**: Workshops seem to be more effective and fun when participants work in teams. Be careful about mixing in-person and virtual attendees together. Consider creating breakout rooms for virtual attendees, with a helper faciliating each room. 
   
4. **Bring enough support**: Ensure a ratio of roughly 1 helper/10 attendees.

5. **Content sharing & local software installation**: Not all employees are able to install software like Compass locally or get to datasets online. If you are going to require content such as dataset files (e.g. the `data/wikipedia_tiny.json`), make sure 1+ attendees run through the prerequisites and workshop content live with you, in the same setting as the workshop will be held in. 
   - Ensure ability to install software locally (if using Compass/the like).
   - Ensure there is an effective, secure, and mutually-approved way for sharing content like installation files and datasets. For example, the workshop sponsor could work internally to provide a secure S3 bucket or a NAS file system path that participants can access before or during the workshop. 

6. **For vector search, compute your vectorized query ahead of time and share in a easy-to-copy way**. See how [here](https://github.com/nickgogan/MongoDBAtlasDeveloperDay/tree/main/data#vectorize-query)

## Troubleshooting Common Issues
1. **Add IP Address to Access List**: MongoDB Atlas clusters only allow connections from known IP addresses. These addresses may change for a variety of reasons, from corporate IT policy rolling them on a regular basis to working on different networks (e.g. home vs corporate network/VPN). To add a new IP address to your Project's Access List via the [Atlas web GUI](https://cloud.mongodb.com/account/login):
    - Log in.
    - Go to "Network Access" on the left-hand panel.
    - Hit the "Add IP Address" button.
    - Add your current IP Address (there should be button to easily do this).
    - Optionally, add a comment to describe your IP address such as "Home" or "Office".
    - Optionally, make the entry temporary (6hrs to 1 week).
    - Allow a few moments for Atlas automation to make the change.
    - Try logging into your cluster using your db user (not your Atlas UI credentials).

2. **Use of VPN**: If attendees MUST be on the VPN, even while in-person, you cannot use the free/shared-tier M0 cluster because a PrivateLink connection must be set up to allow transitive peering for attendees connecting to Atlas via VPN. Transitive peering is necessary in this case and the only way to set this up is by provisioning a paid Atlas cluster and a PrivateLink connection between your customer's network and MongoDB Atlas. 
   - Paid clusters require that some form of billing be configured in the given Atlas Organization.

3. **[Note the free-tier cluster limitations](https://www.mongodb.com/docs/atlas/reference/free-shared-limitations)**