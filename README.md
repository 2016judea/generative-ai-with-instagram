## Generative AI w/Instagram

### Backround

OpenAI (the company that brought us ChatGPT) released an early version of their "vision model" that is capable of understanding images as inputs.

> GPT-4 with vision (GPT-4V) enables users to instruct GPT-4 to analyze image inputs provided by the user

Full research paper and release notes can be found here: https://openai.com/research/gpt-4v-system-card

### Overview

This project joins the power of the GPT-4V LLM with the popular social media platform Instagram.

![system overview](documentation/system_overview.png)

### Results

The responses from GPT-4V were extremely interesting. For example, consider when I asked the following about Kim Kardasian:

```
"input": {
    username: "kimkardashian"
    prompt: "How would you describe this person based on their Instagram posts?"
}
```

And the response from GPT-4V:

```
Based on the Instagram posts provided, this person appears to be multifaceted, with a strong presence in fashion and pop culture. They engage in various activities, represent a brand associated with swimsuits, and seem to embrace high fashion and luxury lifestyles.

The posts suggest an appreciation for fashion design, displayed through both trendy and classic styles. There's also an evident interest in snow sports, as seen in the images of snowboarding and skiing. The person is connected to family and friends, evident in photos shared with others who might be significant in her life. A strong entrepreneurial spirit is noted, with promotional material for a swim shop and reference to a men's underwear line launched in collaboration with a well-known musician whose new album is also mentioned. This suggests an involvement in collaborative brand partnerships and business ventures.

Additionally, there's a clear interest in architecture and design, highlighted by the mention of narrating a home tour for Architectural Digest, which indicates a passion beyond just fashion and entertainment. There are also elements of fun and playfulness, suggested by emojis and a photo capturing a lighthearted moment playing football. Overall, the person portrayed through these Instagram posts is complex with diverse interests spanning business, fashion, recreation, and the arts, with a clear influence on and connection to their social and professional networks.
```

And if you pull up Kim K's profile, you can start to see how the LLM came to this conclusion. For example, consider this reference given in the response above:

> There's also an evident interest in snow sports, as seen in the images of snowboarding and skiing.

Yep, checks out. See this post from Jan 29, 2024:

![instagram post of kim kardashian skiing](documentation/kim_k_skiing.png)

Link to post: https://www.instagram.com/p/C2sUrluxLar/

Let's do another example. Consider the following:

```
"input": {
    username: "tombrady"
    prompt: "Is this Instagram user a celebrity? How can you tell?"
}
```

And the AI's answer:

```
Based on the provided captions and images, it appears that the Instagram user in question is indeed a celebrity. Here are some telling signs:

1. Brand Endorsements: The captions indicate that the user is involved with brand endorsements and advertisements, as seen with references to @tb12sports, @bradybrand, @nobull, and @betmgm. The involvement with multiple brands, especially in the form of sponsored content (#ad), implies a significant public profile and influence.

2. Public Appearances: There are mentions of public appearances and events, such as the announcement of the Hall of Excellence at the Fontainebleau Las Vegas and the first ever @betmgm Big Game ad. This suggests that the user is a prominent figure who participates in events that garner public attention.

3. Collaborations with Other Brands: The user collaborates with well-known brands and platforms such as Meta, as seen in the caption about partnering with Meta to bring a new AI named Bru.

4. Lifestyle: Images and captions suggest a lifestyle that includes travel, meetings with notable individuals, and having a personal brand. This lifestyle is consistent with that of a celebrity.

5. Personal Achievements: References are made to a personal collection of sports memorabilia at a museum, signifying noteworthy achievements that are recognized and celebrated publicly.

6. Influence and Messaging: There is a post regarding a significant international issue, which reflects the user's platform and ability to reach out to a wide audience on important matters
```

Pretty wild right??!!

### For Developers

#### Setup

1. Get your OpenAI developer key

   - Start by following these steps: https://platform.openai.com/docs/quickstart/account-setup
   - Then put your API key into the app.py file locally

2. Set OS environment variables

```
set USERNAME=YOUR_INSTAGRAM_USERNAME    # use export if on Mac/Linux
set PASSWORD=YOUR_INSTAGRAM_PASSWORD    # use export if on Mac/Linux
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Pull down my personal fork of the (previously outdated) Instagram web crawler

```
git clone https://github.com/2016judea/instagram_crawler.git
```

5. Start the server

```
flask run
```

6. Load the UI

Navigate here in your web browser: http://localhost:5000/. The result should look something like this:

![user_interface](documentation/user_interface.png)

### References

- OpenAI Quickstart Guide: https://platform.openai.com/docs/quickstart?context=python
- And a big thanks to huaying's Instagram Web Crawler (needed some changes, but was a great starting point): https://github.com/huaying/instagram-crawler

### Warning

Meta has purposefully made the public Instagram APIs require user permission when accessing data as a means of protecting user privacy. This project uses a (publicly available) web crawler as a workaround to this and should not be used for any means beyond experimental.

Permissions Reference for Meta APIs: https://developers.facebook.com/docs/permissions/
