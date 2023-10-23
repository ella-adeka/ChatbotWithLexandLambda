# CHATBOT WITH LEX AND LAMBDA

## PROMPT
Build a chatbot using Amazon Lex and AWS Lambda. Create a conversational interface that can answer common questions or perform specific tasks. Integrate the chatbot with a messaging platform like Facebook Messenger or Slack.

## ARCHITECTURE DIAGRAM

## STEPS
1. Navigate to Lex
2. Create a bot
    - Create blank bot
    - Enter Bot name as "SupportBot
    - Under IAM permissions
        - Seclect "Create a role with Amazon Lex"
    - Under Children’s Online Privacy Protection Act (COPPA)
        - Choose No
    - Click Next
    - Select Language
    - Choose Voice Interaction eg English (US)
    - Click Done

    - Intent: New Intent
        - Intent Details
            - Enter "SupportIntent" as Intent name
        - Add Sample utterances (utterances, are what the user can use to start interaction with the chatbot)
            - Type an Utterance eg hello, hi
            - Click Add utterance
        - Toggle "Confirmation" to active
        - Same with Closing response
        - Under Confirmation, 
            - enter the following in the confirmation prompt:
                "Can I go ahead with your request?"
            - enter the follwing in the decline prompt:
                "Okay, your request will not be submitted."
        - 
        - Under Closing response
            - enter the message as: (response chatbot will give when the user starts interacting with their utterances)
                Thanks!
            - (Optional) can add variations to spice things up
                - Click "More responses under Variations
                    - The closing message editor will pop up 
                    - Click on the variations dropdown and enter "Thank you!"
                    - Click Update responses
        - Save Intent

        * Slots are placeholders for the user input

        - Navigate back to intents list
        - In the Amazon Lex menu, click "slot types" under OrderPizza
            -Click Add slot type dropdown
                - Click "add blank slot type"
            - Specify Slot type name
                - Enter "PizzaType" as Slot type name
                - Click Add
            - Under Slot value resolution
                - Select "Restrict slot values"
            - Under slot type values
                - Under value, enter "Italian"
                - for its corresponding values, enter italian, italy,Italy
                * click tab or ; after each value, for a new one
                - You can add more values like "Mexican", with corresponding values like "mexico", "mexican" etc
            - Save Slot type

            - Navigate back to Slot types
                - Create two more: PizzaCrust and Appetizer

        - Navigate back to Intent: OrderPizza
        - Slots
        - Add slot
            1. Name: Name
                Slot type: AMAZON.firstname
                Prompts: Hello! May I know your first name
        - Click add
        - add more slots:
            - Pizza Type
                - name: PizzaType
                - slot type: pizzatype
                - prompts: {Name}, What pizza would you like to order? 

            * Add custom value by putting the slot name in {} eg {Name}

        - scroll up to Conversational flow to see how the conversation will go

        - Save intent

        - Improve UI by adding values
            - Choose DeliveryTime option
                - click advanced options
                - scroll down to slot prompts
                - click bot elicits information DROPDOWN
                - cLICK more prompt options
                - toggle preview
                -click add
                    -add card group
                    - update card
                        - enter title as "Available times" as placeholder
                        - click buttons fropdown
                            click add button
                                - button 1 title : 20:00
                                - button 1 value : 8pm

                                - button 2 title : 20:30
                                - button 2 value : 8:30pm
                    - click "update prompts"
                    - click update slot
        
        - Save intent

        - Click Build

        - Test
3. Navigate to Slack  
    - Create an workspace
        - https://slack.com/
        - Click Try for free
        - Enter your mail
        - Create workspace
        - Step 1: Enter the name of your company or team
        - Step 2: Enter your name
        - Step 3: Skip "Who else is on the SupportTees team"
        - Step 4: Enter "SupportBot for Teesside Uni" as what ypur team is working on
4. Navigate to slack api
    - https://api.slack.com/
    - Click "Your app" at the top right corner > Create ypur first app
    - Select "From Scratch"
    - Name app & choose workspace
        - Enter "SupportTeesBot" as app name
        - Select "SupportTees" as workspace
        - Create App
    - Go to Setting > Basic Information
    - Scroll down to App Credentials
    - Copy the following credentials from slack api and paste in Lex console: add channel
        - Client ID
        - Client Secret
        - Verification token
    - In the Lex console, click "Add"
5. Configure Integrativity & Shortcuts
    - Go to Features > Integrativity & Shortcuts
    - Toggle on
    - Paste "https://slack.com" as the Request URL (temporarily)
    - Save changes
6. Set up the OAuth Endpoint
    - Navigate back to the Lex console
    - Click the newly created channel
    - Scroll down to OAuth endpoint, and copy it
    - Navigate back to slack api
    - Go to Features > OAuth & Permissions
    - Add new redirect URL
        - Paste
        - Click Add
        - Click Save URLS
    - Scroll down to Scopes
        - Under Bot Token Scopes, click Add OAuth scope
        - Add:
            - chat:write
            - team:read
    - Navigate back to Lex and copy Endpont url
    - Backl to slack api > features > interactivity & shortcuts
        -Replace the temporary url with the endpoint url
        - Save changes
7. Events & Subscriptions
    - Toggle Enable events

8. Channel Integrations
    - Select "Slack" as platform
    - Leave IAM role as is, assuming its the Amazon Lex role
    - Under Integration configuration
        - Enter "SupportTees" as Name
        - Enter "Customer support for prospective TU students" as the description
        - Select "TestBotAlias as Alias
        - Select "English (US) as Language (should be the same as what was 
        chosen when creating the bot)
    


## RESULTS