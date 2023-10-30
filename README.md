# MongoDB Atlas Developer Day Workshop

This hands-on workshop is meant to introduce developers new to MongoDB and MongoDB Atlas to how the database works.

- **Last Updated:** October 30th, 2023
- **Owner:** [Nick Gogan](nick.gogan@mongodb.com) (feel free to reach out!)

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

5. **Add your IP address**:
   - Scroll down and keep the default "My Local Environment".
   - Hit "Add My Current IP Address" to your current IP address to the IP Access List of your Atlas Project. 
   - Scroll down to the bottom of the page and hit "Finish and Close".

6. You will be presented with a small pop - select "Go to Overview" to see your M0 cluster being provisioned from your chosen cloud provider, in your selected region. Depending on the cloud provider and region, this can take anywhere from 10-20min. 

7. **Your are aready for the workshop!**

## Workshop Facilitator Checklist