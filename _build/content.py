"""
Portfolio content. Every figure here comes from the campaign notes, the
CV, Ramtin's own notes in conversation, the Google Cloud account reports,
or on-screen data in the supplied assets. See _build/SOURCES.md for the
source of each number. Nothing is estimated.

Media references:
  ("v", "name", "caption")   -> assets/media/name.mp4 + name.webp poster
  ("i", "name", "caption")   -> assets/img/work/name.webp
Each media group is a row; items sit side by side at equal height with no cropping.

Text blocks (challenge, role, approach, idea) are lists of:
  "a paragraph"
  ("h", "a subheading")
  ("list", ["<strong>Lead-in.</strong> bullet", ...])     bullets
  ("steps", [("Step title", "what happened"), ...])        numbered steps
"""

LINKEDIN = "https://www.linkedin.com/in/rtotonchi4412"

# --------------------------------------------------------------------------- positioning
HOME_INTRO = "I bridge culture, creativity and strategy to shape ideas that stand out."

ABOUT_LEDE = (
    "I lead social-first creative work: the strategy behind it, the idea at the centre of it, "
    "the content that carries it, and the numbers that show whether it worked."
)

ABOUT_BODY = [
    "I spent twelve years building my own audience as a creator before owning social for anyone else. "
    "Since then, I\u2019ve run social at G2 Esports, shaped EMEA social and creative strategy for VALORANT Esports "
    "at Riot Games, and continued that work at Edelman across nine markets.",
    "Today, I lead social content for Google Cloud at Jellyfish: turning complex technology into work that "
    "executives, engineers and wider audiences actually stop for. I also own the Luminary Programme, "
    "keeping Google Cloud leaders visible and credible on LinkedIn.",
]

STATS = [  # (number, suffix, label) – all verified in SOURCES.md
    (15, "+", "Years in social, content and community"),
    (1000, "+", "Videos delivered between 2020 and 2026"),
    (100, "K", "Scaled a newly launched YouTube channel to 100K subscribers in year one, earning the Silver Creator Award."),
    (2021, "", "Esports Creative Piece of the Year, G2\u00a0Esports\u00a0×\u00a0adidas"),
]

# Account-level results for Google Cloud social (Jellyfish). High-level numbers only.
ACCOUNT_RESULTS = dict(
    title="Google Cloud social, at Jellyfish",
    intro="Account-level results across Google Cloud\u2019s global LinkedIn and Instagram, plus its UK X channel.",
    periods=[
        dict(name="Account year to November 2025",
             scope="LinkedIn (global), Instagram (global) and X (UK)",
             stats=[("5.1M", "Impressions", "+12.6% year on year"),
                    ("601.7K", "Engagements", "+28.8% year on year"),
                    ("265.6K", "Weighted engagements", "+54.1% year on year"),
                    ("11.8%", "Engagement rate", "up from 10.4%")],
             note="Followers across the three accounts grew by 106,534 to 777,064."),
    ],
)

EXPERIENCE = [
    ("Jellyfish", "Social Content Manager, on the Google Cloud account", "2025–now", "london-summit-sizzle"),
    ("Edelman", "Social & Content Lead, on the Riot Games account", "2024–25", "vct24-kickoff-teaser"),
    ("Riot Games", "Social Media Strategist, EMEA · VALORANT Esports", "2022–24", "join-us"),
    ("G2 Esports", "Social Media Manager", "2020–22", "g2-adidas-film"),
    ("Independent", "Content Creator & Consultant", "2008–20", "origin"),
]

BRANDS = ["Google Cloud", "The FA", "Riot Games", "VALORANT Esports", "adidas", "Ralph Lauren", "Logitech G",
          "Red Bull", "Aim Lab", "Cougar", "Paysafecard", "Unilumin", "OMEN by HP", "Intel", "Snickers"]

# --------------------------------------------------------------------------- shared role copy
JF = ("As Social Content Manager at Jellyfish and Social Content Lead on the Google Cloud account, I own content output end to end, "
      "from brief ingestion and creative direction through production, approvals and publishing, across Google Cloud and its partner portfolio.")
ED = ("As Social & Content Lead at Edelman on the Riot Games account, I owned the creative and content pipeline for VALORANT Esports across "
      "EMEA: shaping briefs, setting creative direction, steering production partners and reporting performance back to senior stakeholders across nine markets.")
RG = ("As Social Media Strategist, EMEA at Riot Games, I owned the social and creative strategy for VALORANT Esports in the region, "
      "connecting audience insight with global brand objectives and taking campaigns from brief to launch to measurement.")

# --------------------------------------------------------------------------- case studies
# via: how Ramtin was involved: employer or agency, so client and employer are never confused
P = []

P.append(dict(
    slug="google-cloud-london-summit", featured=True,
    title="London Summit 2026", client="Google Cloud", via="At Jellyfish", year="2026",
    platforms="LinkedIn, X, Instagram, Facebook", cat="B2B event campaign",
    thumb=("v", "london-summit-sizzle"), quote="From live event to week-long conversation.",
    summary="An earned and owned social campaign built to make Google Cloud's London Summit the UK's reference point for AI and data cloud, "
            "and to make the day's content keep working long after the keynote ended.",
    challenge=["The brief was explicit: establish Google Cloud as the leading authority in AI and data cloud in the UK market. "
               "Every major cloud provider was making that claim, to the same audience of technical and business decision-makers.",
               "Event content usually peaks on the day and disappears. The challenge was to turn one summit into authority that "
               "showed up in owned channels, in people's own feeds, and in trade media."],
    role=[JF,
          "On the Summit, I led the social content workstream: translating the mission statement into a channel plan, "
          "aligning the Google Cloud team, Jellyfish strategists and production partners on one content roadmap, "
          "briefing the on-site capture, and keeping executive, advocacy and brand content moving at the speed of a live event. "
          "After the day, I tracked performance against the KPIs for each layer and fed the learnings into the next activation."],
    approach=["A full-funnel social ecosystem, with every layer given its own job and its own KPI:",
              ("steps", [("Define the job", "One mission: authority in AI and data cloud in the UK. Every asset had to ladder up to it."),
                         ("Owned builds authority", "LinkedIn, X, Instagram and Facebook carry the brand narrative, measured on weighted engagement rather than vanity reach."),
                         ("Earned builds trust", "Employee advocacy through Halo, creators and the executives in the Luminary Programme put real voices behind the message, measured on share of voice and reach."),
                         ("Paid builds scale", "TechTarget and Condé Nast extend the story to in-market decision-makers, measured on impressions and sentiment."),
                         ("Capture once, publish everywhere", "On-site capture designed for every layer at once, so one moment from the stage becomes a brand post, an executive update, an employee share and a paid placement."),
                         ("Read and optimise", "Live monitoring on the day, then a full read-out against target to sharpen the next event.")])],
    idea=["Treat the Summit as a content studio, not just a stage. Executives, speakers and Gemini masterclass sessions were captured on the day "
          "as platform-native video and stories, then distributed through every layer above. The campaign's own line put it simply: "
          "don't just capture your event, scale it."],
    delivered=["Owned, earned and paid channel strategy with a KPI per layer",
               "Executive and speaker videos filmed at the Summit",
               "Live and on-the-day content across LinkedIn, X, Instagram and Facebook, including Instagram Stories",
               "Employee advocacy and executive amplification through Halo and the Luminary Programme",
               "Results reel summarising the campaign"],
    results=[("611K", "Impressions", "+138% year on year"),
             ("29.5K", "Weighted engagements", "26% above target"),
             ("4.1M", "Earned impressions", "+144% year on year"),
             ("5,512", "Earned mentions", "+445% year on year"),
             ("455K", "Employee-advocacy reach", "680× year on year"),
             ("71K", "Impressions from a single Instagram Story", "")],
    results_note="Figures as reported in the campaign's results reel.",
    skills=["B2B social strategy", "Owned, earned and paid planning", "Event content", "Executive and employee advocacy", "Performance measurement"],
    media={"hero": [("v", "london-summit-sizzle", "Results reel, London Summit 2026")],
           "after_approach": [("v", "london-summit-alex-rutter", "Alex Rutter, EMEA Managing Director, AI, Google Cloud, filmed at the Summit"),
                              ("v", "exec-maureen-drone-challenge", "Maureen Costello on drone technology and supply chains"),
                              ("v", "exec-joana-deepmind", "Joana Carrasqueira, Google DeepMind, on vibe coding")]},
))

P.append(dict(
    slug="the-fa-x-google-cloud", featured=True,
    title="The FA × Google Cloud", client="The FA · Google Cloud", via="At Jellyfish", year="2026",
    platforms="Vertical social video (9:16)", cat="Partnership content",
    thumb=("composite", ["fa-roboball", "fa-creative-agent", "fa-get-to-know"]), quote="Robot football, powered by Gemini.",
    summary="A vertical video series that put England players in front of Google Cloud's AI tools, so football fans could see what Gemini does by watching players compete with it.",
    challenge=["AI products are abstract, and sports partnership content often ends up as players standing next to a logo. "
               "This had to engage a football audience in a conversation about AI, and feel high-energy and playful rather than like a product demo."],
    role=[JF,
          "On this partnership I was part of the core team that developed the hero concepts: pressure-testing each idea for social, "
          "shaping the formats around what talent time allowed, and owning how the series would land on platform. I then steered the work "
          "through production, edit and approvals with the client, The FA and our production partners."],
    approach=["Product-led storytelling, disguised as play:",
              ("steps", [("Find the tension", "Football fans don't care about AI features, but they love competition, banter and seeing players off-guard."),
                         ("Make the product the game", "Each hero concept turns one Gemini capability into a challenge, so the tech is understood by watching it work, not by being told."),
                         ("Build a content system", "Two hero films carry the product story; lighter quick-fire formats deliver personality, frequency and cut-downs between them."),
                         ("Design for the feed", "Vertical-first, hook in the opening seconds, split screens, stat cards, captions and sound design built for sound-off and sound-on viewing."),
                         ("One shoot, many assets", "Plan the formats around a single block of player access to maximise output per minute of talent time.")])],
    idea=[("h", "AI RoboBall"),
          "Robot football powered by Gemini. Each robot starts with a basic Python program. The players improve it by telling Gemini how the robot should play, "
          "and Gemini Code Assist turns their instructions into code using its knowledge of the game and the robot's API. "
          "A three-minute countdown, GoPros on the players for split-screen footage and stat cards for each player build the drama before kick-off.",
          ("h", "Creative Agent drawing challenge"),
          "Players draw to a football theme, then the Creative Agent uses Veo and Imagen to turn each sketch into an image and a short video. "
          "Split screens capture the drawings and the reactions, and the players judge whose creation best fits the brief.",
          ("h", "Quick-fire formats"),
          "Overrated or Underrated, and a Get to Know format of fast, culturally relevant questions, to show more of who the players are."],
    delivered=["AI RoboBall hero film", "Creative Agent drawing challenge hero film", "Overrated or Underrated", "Get to Know quick-fire", "A quick-fire numbers guessing game"],
    results=[],
    results_note="Performance data for this series wasn't part of the material supplied, so none is shown here. What's shown is the delivered work: two hero concepts and three quick-fire formats.",
    skills=["Creative concepting", "Brand partnerships", "Talent-led content", "Explaining complex technology", "Vertical video"],
    media={"hero": [("v", "fa-roboball", "AI RoboBall"), ("v", "fa-creative-agent", "Creative Agent drawing challenge")],
           "after_delivered": [("v", "fa-over-under", "Overrated or Underrated"), ("v", "fa-get-to-know", "Get to Know"), ("v", "fa-quickfire-numbers", "Quick-fire numbers game")]},
))

P.append(dict(
    slug="luminary-programme", featured=True,
    title="The Luminary Programme", client="Google Cloud", via="At Jellyfish", year="2025–now",
    platforms="LinkedIn", cat="Executive social",
    thumb=("composite-light", ["luminary-1", "luminary-4", "luminary-2"]), quote="Executives, heard on their own terms.",
    summary="An always-on programme that gives Google Cloud's senior leaders a consistent, credible presence on LinkedIn, with zero self-briefing for the executives and end-to-end ownership by me.",
    challenge=["Senior leaders are the most trusted voices a B2B brand has, and the hardest to get publishing. Executive content tends to be sporadic, "
               "drift off-message, or sit in a folder approved but never posted.",
               "The measure that matters isn't how many assets get made. It's how many get published, by the right person, at the moment the business needs them."],
    role=["I lead the Luminary Programme end to end at Jellyfish. That covers programme strategy and editorial planning, "
          "executive onboarding and relationship management, voice-of-leader copywriting and creative, governance and permissions in Sprinklr, "
          "scheduling and native publishing, and reporting on adoption and performance back to the Google Cloud team.",
          "Day to day, I'm the single point of contact between the executives' teams and the content engine, which is what makes zero self-briefing possible."],
    approach=["A thought-leadership operating model built for adoption, not output:",
              ("steps", [("Map the voices", "Match each executive to the themes, products, regions and audiences they can credibly own."),
                         ("Plug into the business calendar", "Align the editorial plan with product launches, priority company announcements, customer stories, partner milestones, regional news and field and industry events."),
                         ("Remove the friction", "Zero self-briefing: executives receive ready-to-publish posts and creative in their own voice, with nothing to write or brief."),
                         ("Publish natively", "Posts go out from executives' own profiles, managed by Jellyfish in Sprinklr with the right permissions, scheduling and milestones."),
                         ("Measure adoption", "Track what was published and adopted, not just produced, and refine angles and cadence from the data.")])],
    idea=["One moment, many credible voices. Around a launch like Gemini at Work '26, each executive takes the angle that fits their remit: "
          "productivity for the UK, Ireland and Sub-Saharan Africa CEO, financial services for the EMEA AI lead, engineering, security and digital sovereignty for others. "
          "The audience gets five different reasons to care instead of one press release repeated five times."],
    delivered=["Always-on executive content calendar", "Post copy and creative tailored to each executive",
               "Native publishing on executives' own profiles via Sprinklr", "Coordination with each executive's point of contact",
               "Amplification of launches, customer stories, partner milestones and regional moments"],
    results=[],
    results_note="Programme-level metrics weren't included in the supplied material. The evidence shown is the published work: coordinated posts from five Google Cloud executives around Gemini at Work '26.",
    skills=["Executive social", "Thought leadership", "B2B LinkedIn", "Programme management", "Stakeholder management", "Sprinklr"],
    media={"hero": [("i", "luminary-1", "LinkedIn post by Maureen Costello, Google Cloud, about Gemini at Work"),
                    ("i", "luminary-4", "LinkedIn post by Alex Rutter, Google Cloud, about Lloyds Banking Group and Gemini Enterprise"),
                    ("i", "luminary-2", "LinkedIn post by Chris Lindsay, Google Cloud, about Merck and Gemini Enterprise")],
           "after_approach": [("i", "luminary-3", "LinkedIn post by Dr. Marianne Janik, Google Cloud, about digital sovereignty"),
                              ("i", "luminary-5", "LinkedIn post by Ben Cabanas, Google Cloud, about Gemini agent")]},
))

P.append(dict(
    slug="vct-emea-tiktok-launch", featured=True,
    title="VCT EMEA on TikTok", client="Riot Games", via="At Edelman", year="2024",
    platforms="TikTok", cat="Platform launch",
    thumb=("composite", ["tiktok-clip-1", "tiktok-clip-2"]), quote="Zero to 100K in year one.",
    summary="The launch of VCT EMEA's TikTok channel, built on native content captured with players and talent, which grew to 100,000 followers in its first year.",
    challenge=["A new channel starts at zero, and TikTok audiences scroll past anything that looks like a repurposed broadcast clip. "
               "Player time is limited across a season, so native content had to be planned rather than hoped for."],
    role=[ED,
          "I owned the TikTok launch campaign end to end: the channel strategy and content pillars, the shot lists and formats for media day, "
          "on-site direction with players and talent, and the publishing cadence and optimisation through the first year."],
    approach=["A platform-first launch playbook:",
              ("steps", [("Start native", "No repurposed broadcast clips. Every launch asset is written for the For You page."),
                         ("Piggyback on access", "Use media day, when evergreen content for the year is captured, to also capture TikTok-native shorts with players and talent."),
                         ("Build content pillars", "Trends, personality and behind-the-scenes formats that can be repeated and scaled across the year."),
                         ("Test, learn, double down", "Read what the algorithm rewards and put more behind the formats that break out.")])],
    idea=["Content that works on the For You page first and feels true to the people in it: short, self-aware formats and trends performed by the players and talent themselves."],
    delivered=["TikTok launch campaign", "Native shorts planned and captured at media day", "Ongoing organic publishing through the first year"],
    results=[("100K", "Followers in the first year", ""),
             ("~10M", "Total views", "Several videos reached millions"),
             ("~4M", "Views on the top video of 2024", ""),
             ("380K", "Engagements", "")],
    results_note="",
    skills=["Platform launch", "Short-form video", "Organic growth", "Production planning", "Talent-led content"],
    media={"hero": [("v", "tiktok-clip-1", "TikTok-native short filmed at media day"), ("v", "tiktok-clip-2", "TikTok-native short filmed at media day")]},
))

P.append(dict(
    slug="push-to-talk", featured=True,
    title="Push to Talk × Logitech G", client="Riot Games · Logitech G", via="In-house, then at Edelman", year="2023–24",
    platforms="YouTube, X", cat="Sponsored series",
    thumb=("v", "push-to-talk-2023"), hero=("v", "push-to-talk-2024"), quote="Hear the game the players hear.",
    summary="A sponsored series I created with Logitech G: mic-check content that lets fans hear players talk in and out of the game as they prepare, set up and compete.",
    challenge=["Sponsor content in esports is easy to skip. Logitech needed an integration that made sense for a headset and microphone brand "
               "and that fans would actually want to watch."],
    role=["I created Push to Talk and owned it end to end: the format, the partnership pitch and working relationship with Logitech, "
          "comms capture and edit direction, publishing, and performance reporting to the partner. "
          "I launched it at Riot Games in 2023 and redesigned the format, structure and layout at Edelman in 2024."],
    approach=["Branded content where the product is the point of view:",
              ("steps", [("Start from the product truth", "Logitech makes the headsets and microphones players use, so the content should be about what you hear through them."),
                         ("Make the integration the format", "Mic-check content can't exist without the product, so the brand never feels bolted on."),
                         ("Give fans something new", "Comms, calls and banter they can't get from the broadcast alone."),
                         ("Amplify with paid", "Logitech sponsored the series and put paid support behind it."),
                         ("Iterate the format", "A redesigned structure and layout in year two, built on what the 2023 data told us.")])],
    idea=["Push to Talk: a mic-check format. Player comms, banter and calls during matches, cut together so fans hear the game the way the players do."],
    delivered=["Seven-episode series in 2023", "A redesigned format, structure and layout in 2024", "Paid support in partnership with Logitech"],
    results=[("300K", "Views, 2023 series", "7 episodes"), ("21K", "Engagements, 2023 series", ""), ("~50%", "Better performance in 2024", "vs the 2023 series")],
    results_note="",
    skills=["Format creation", "Brand partnerships", "Sponsor integration", "Paid and organic", "Series development"],
    media={"hero": [("v", "push-to-talk-2023", "Push to Talk, 2023")],
           "after_delivered": [("v", "push-to-talk-2024", "Push to Talk, 2024 episode")]},
))

P.append(dict(
    slug="vct-emea-bootcamp", featured=True,
    title="VCT EMEA Bootcamp", client="Riot Games", via="In-house", year="2023",
    platforms="X, Instagram, YouTube · paid social", cat="Paid and organic sign-up campaign",
    thumb=("v", "vct-bootcamp"), quote="80,000 fans, matched with the pros.",
    summary="A personalised fan experience that turned each player's own VALORANT data into a bespoke Bootcamp video and matched them with a VCT EMEA pro, driven by a joint social, media and paid campaign.",
    challenge=["The goal was simple and measurable: get as many people as possible to sign up for their bespoke Bootcamp data, "
               "in a feed already crowded with esports content."],
    role=[RG,
          "On Bootcamp my role was creative input and social campaign planning: shaping how the experience would be presented on social, "
          "building the organic rollout and reminders, and working jointly with the media and paid teams so organic and paid pushed toward one sign-up goal."],
    approach=["A personalisation-led acquisition campaign:",
              ("steps", [("Make the fan the hero", "Each person gets a video built from their own data, which is worth sharing."),
                         ("Give them a pro to compare with", "Matching fans with a VCT EMEA pro links the experience back to the league."),
                         ("Run organic and paid as one", "Joint planning with media and paid, with every touchpoint driving to the sign-up page."),
                         ("Use urgency", "Last-chance reminders before the experience closed.")])],
    idea=["VCT EMEA Bootcamp: create your personalised video and compare yourself with the pros."],
    delivered=["Social campaign plan and organic rollout", "Creative input on the experience and launch assets", "Joint campaign with media and paid", "Reminder posts ahead of close"],
    results=[("80K+", "Sign-ups for a bespoke Bootcamp video", ""), ("23.4K", "Views on a single last-chance reminder post on X", "")],
    results_note="",
    skills=["Paid and organic", "Personalisation", "Acquisition", "Campaign planning", "Cross-team collaboration"],
    media={"hero": [("v", "vct-bootcamp", "VCT EMEA Bootcamp"), ("i", "bootcamp-tweet", "VALORANT Esports EMEA post on X: last chance to create your #VCTBOOTCAMP2023 personalised video")]},
))

P.append(dict(
    slug="g2-esports-x-adidas", featured=True,
    title="G2 Esports × adidas", client="G2 Esports · adidas", via="In-house", year="2021",
    platforms="X, YouTube, Instagram · organic and paid", cat="Partnership launch",
    thumb=("i", "g2-adidas-newspaper"), hero=("i", "g2-adidas-shopfront"), quote="Esports Creative Piece of the Year, 2021.",
    summary="The integrated social launch of adidas as G2 Esports' official sports apparel partner, which won Esports Creative Piece of the Year in 2021.",
    challenge=["Announcing a kit partner is usually a logo lockup and a press release. adidas joining the #G2ARMY meant a pro jersey, a lifestyle collaboration and new content, "
               "and the launch had to feel as big as that, for gaming fans and sportswear fans at the same time."],
    role=["As Social Media Manager at G2 Esports, I developed the integrated social creative campaign for the launch across organic and paid social: "
          "the campaign platform, the rollout across X, YouTube and Instagram, coordination with the adidas team and G2's creative and partnerships teams, "
          "and community management and reporting through launch."],
    approach=["An integrated launch that respects both fanbases:",
              ("steps", [("Find the overlap", "Blend athletic and gaming-inspired creative so the partnership feels native to both worlds."),
                         ("Make it an event", "A cinematic announcement film as the centrepiece."),
                         ("Go native on every platform", "Tell the story the way each platform works, not one asset pushed everywhere."),
                         ("Extend the moment", "Behind-the-scenes films on YouTube and a 2021 pro jersey reveal to keep the story going after day one."),
                         ("Organic and paid together", "Paid support to take the launch beyond the existing #G2ARMY.")])],
    idea=["Treat the partnership like breaking news in G2's world: a cinematic announcement film, with the tie-up written up as a front-page headline."],
    delivered=["Announcement film", "2021 pro jersey reveal video", "Behind-the-scenes films on YouTube", "Campaign photography", "Organic and paid social rollout"],
    results=[("2.7M", "Views", "X, YouTube and two behind-the-scenes films"), ("60K+", "Engagements", "Likes, reposts, comments and bookmarks"), ("2.2%", "Engagement rate", "Engagements ÷ views"), ("2021", "Esports Creative Piece of the Year", "")],
    results_note="On X alone: 2M views, 43,000 likes, 4,700 reposts, 656 comments and 200 bookmarks. On YouTube: 600,000 views, 10,000 likes and 373 comments.",
    skills=["Integrated campaign", "Brand partnerships", "Organic and paid social", "Creative direction", "Platform-native storytelling"],
    media={"hero": [("v", "g2-adidas-film", "G2 Esports × adidas announcement film")],
           "after_approach": [("i", "g2-adidas-newspaper", "Campaign photography: the partnership as front-page news"), ("i", "g2-adidas-onset", "On set for the announcement film")],
           "after_idea": [("i", "g2-adidas-shopfront", "Campaign photography"), ("i", "g2-adidas-shelf", "Campaign photography: the 2021 jersey")],
           "after_delivered": [("v", "g2-adidas-jersey", "G2 Pro Kit Jersey 2021 reveal")]},
))

P.append(dict(
    slug="pink-pony-streamathon", featured=True,
    title="Pink Pony Streamathon", client="G2 Esports · Ralph Lauren", via="In-house", year="2021",
    platforms="Twitch, X, Instagram", cat="Charity live event",
    thumb=("i", "pink-pony-together"), quote="552K live viewers for a good cause.",
    summary="The first Pink Pony Streamathon: a three-hour live charity event from Berlin with G2 Esports and Ralph Lauren, supporting young people with cancer at The Royal Marsden.",
    challenge=["A new addition to Ralph Lauren's long-running Pink Pony campaign, so there was no previous event to build on. It needed a live audience big enough to matter "
               "and a tone that respected the cause while still feeling like a G2 stream."],
    role=["As Social Media Manager at G2 Esports, I managed both the social campaign and the broadcast operations: the promotional rollout and line-up announcements, "
          "run-of-show and live production coordination on the night, real-time community management, and post-event highlights and reporting to the partner."],
    approach=["A cause-led live event, run like a flagship broadcast:",
              ("steps", [("Build anticipation", "Announce players, hosts and music in the run-up, like any G2 event."),
                         ("Make the stream the content", "Player challenges, live music and hosts in one three-hour show."),
                         ("Keep the cause visible", "Donations open throughout the evening, with the purpose front and centre."),
                         ("Extend the moment", "Highlights content after the event to thank the community and the partner.")])],
    idea=["A streamathon: G2 players competing in challenges live from LVL World of Gaming in Berlin, with live music, hosts and donations, on 27 October 2021."],
    delivered=["Social promotion campaign and line-up announcements", "Broadcast operations for the three-hour live show on Twitch", "Highlights content after the event"],
    results=[("552K", "Live unique viewers", ""), ("£5,971.44", "Raised with the #G2ARMY", ""), ("10K", "Engagements", "")],
    results_note="Funds support roles at The Royal Marsden's Oak Centre for Children and Young People, including play specialists, psychologists and complementary therapists.",
    skills=["Live broadcast", "Cause-led campaign", "Brand partnerships", "Community"],
    media={"hero": [("v", "pink-pony-highlights", "Pink Pony Streamathon highlights")],
           "after_approach": [("v", "pink-pony-promo", "Line-up announcement"), ("i", "pink-pony-keyart", "Ralph Lauren Pink Pony × G2 key art")],
           "after_delivered": [("i", "pink-pony-team", "G2 players and hosts at the Pink Pony Streamathon in Berlin")]},
))

P.append(dict(
    slug="origin-and-the-creator-years", featured=True,
    title="Origin, and the Creator Years", client="Independent", via="Self-employed", year="2008–20",
    platforms="YouTube, Twitch, X, Discord", cat="Creator and community",
    thumb=("v", "origin"), quote="Before the brands, the audience.",
    summary="Twelve years making my own content, from gaming montages to full-time streaming. It's where I learned what makes people watch, share and come back.",
    challenge=["As an independent creator there's no media budget and no brand to borrow attention from. Every view has to be earned through the work itself, and the community has to want to come back."],
    role=["Creator, producer, editor and community lead, all at once: concept, capture, edit, publishing, scheduling and the whole content pipeline, "
          "plus community building across Discord, YouTube and X and brand partnerships with OMEN by HP, Intel and Snickers. "
          "I also competed at events including TwitchCon and EGX."],
    approach=["Audience growth without a media budget:",
              ("steps", [("Make every piece an event", "Montages edited to be watched, rewatched and shared."),
                         ("Build a home for the community", "Discord, YouTube and X as places people come back to, not just channels."),
                         ("Show up consistently", "380 streams and 2,187 hours live in 2018 alone."),
                         ("Grow year on year", "Use the data to see what's working and do more of it.")])],
    idea=["Origin, a Call of Duty montage that was groundbreaking for its time and got the attention of notable creators including KSI."],
    delivered=["Origin and other gaming montages", "Live streaming: 380 streams in 2018", "Community across Discord, YouTube and X", "Brand relationships with OMEN by HP, Intel and Snickers"],
    results=[("61K", "Views, Origin", "6,500 engagements"), ("49K", "Views, Blood // Water", "1,400 likes"), ("25K", "Views, Gears of War 3 Montage #1", "800 likes")],
    results_note="Streaming results for 2018 are below.",
    creator=True,
    skills=["Content creation", "Editing", "Community building", "Live streaming", "Brand partnerships"],
    media={"hero": [("v", "origin", "Origin")],
           "after_idea": [("i", "origin-ksi-comment", "KSI's comment on Origin"), ("i", "montage-fortnite", "Blood // Water, a Fortnite montage: 49K views, 1,400 likes"), ("i", "montage-gow3", "Gears of War 3 Montage #1: 25K views, 800 likes")]},
))


# --------------------------------------------------------------------------- VALORANT Esports hub pages
# The VALORANT Esports work is grouped by season (and Masters events) so the portfolio reads as a story, not 15 cards.
# A hub has chapters; each chapter has feature "pieces" (text column + media rows) and optional "compact" items
# (title, media name, kind, description, stat[, anchor id]).

P.append(dict(
    slug="valorant-masters", featured=True,
    title="VALORANT Masters", client="Riot Games", via="In-house, then at Edelman", year="2023–24",
    platforms="X, Instagram, YouTube, TikTok", cat="International event campaigns",
    thumb=("grid", ["tokyo-fnatic", "masters-madrid-hello", "tokyo-liquid", "road-to-masters-tokyo"]), hero=("i", "tokyo-winners"),
    quote="Drawn for Tokyo, written for its fans.",
    summary="EMEA's social campaigns for two VALORANT Masters events: Tokyo in 2023, which I led in-house at Riot Games and is the campaign "
            "I'm proudest of, and Madrid in 2024, where I set the creative direction at Edelman.",
    challenge=["International events compete with everything else in the esports calendar. Each Masters had to feel unmissable to EMEA's fans, "
               "and give the host city a real role in the story rather than a backdrop for logos and dates."],
    role=["I led EMEA's social campaign for Masters Tokyo in-house at Riot Games in 2023, and set the creative direction for the Masters Madrid "
          "hype film at Edelman in 2024."],
    approach=["Start from the host city:",
              ("steps", [("Make the city a character", "Tokyo's visual culture and Madrid's streets carry the story, not the event branding alone."),
                         ("Work with the people who know it", "For Tokyo, Riot Games' Tokyo office shaped how the campaign spoke to Japanese fans."),
                         ("Give fans something to keep", "Assets that outlive match day, like wallpapers of every team."),
                         ("Stay on through the final", "Coverage that keeps the campaign going until the trophy is lifted.")])],
    idea=None,
    results=[("1M", "Impressions across static assets", "Masters Tokyo"), ("200K+", "Views across video", "Masters Tokyo"), ("10K+", "Engagements", "Masters Tokyo")],
    results_note="", delivered=[],
    chapters=[
        dict(id="tokyo", title="Masters Tokyo, 2023", intro="The first VALORANT Masters held in Japan, and the campaign I'm proudest of from my time on VALORANT Esports.",
             pieces=[dict(id="road-to-masters-tokyo", kicker="In-house at Riot Games", title="Drawn for Tokyo, written for its fans",
                          text=["EMEA's four teams, Fnatic, Team Liquid, NAVI and FUT Esports, drawn as bespoke anime-style illustrations: a visual language "
                                "that belongs to the host city, carried through the event in several forms, from the Road to Masters film and team artwork "
                                "to wallpapers and match-day coverage.",
                                ("h", "Written for Japanese fans"),
                                "We worked with Riot Games' Tokyo office so the campaign would land with Japanese audiences. Together we compiled the phrases "
                                "and slang the Japanese VALORANT community uses, each one approved by the Tokyo office, and that language ran through all of "
                                "our social copy during event coverage.",
                                ("h", "Something to keep"),
                                "Desktop and mobile wallpapers of each team carried the event beyond match days, and when Fnatic took the title, a winners' "
                                "wallpaper marked it."],
                          role="I led EMEA's social campaign: the illustrated team assets, the localisation work with Riot Games' Tokyo office, and coverage "
                               "across the event, from the Road to Masters film through to the winners' wallpaper for Fnatic.",
                          stats=[("1M", "Impressions across static assets"), ("200K+", "Views across video"), ("10K+", "Engagements")],
                          note="Engagement and positive sentiment from Japanese fans rose sharply across X, YouTube community posts and Instagram. "
                               "The campaign served the local community and the global one at the same time.",
                          media=[[("v", "road-to-masters-tokyo", "Road to Masters Tokyo")],
                                 [("i", "tokyo-fnatic", "Fnatic, illustrated for Masters Tokyo"), ("i", "tokyo-liquid", "Team Liquid, illustrated for Masters Tokyo")],
                                 [("i", "tokyo-navi", "NAVI, illustrated for Masters Tokyo"), ("i", "tokyo-fut", "FUT Esports, illustrated for Masters Tokyo")],
                                 [("i", "tokyo-final", "Match-day coverage: the final, Fnatic vs EG"), ("i", "tokyo-winners-mobile", "Winners' mobile wallpaper for Fnatic")]])]),
        dict(id="madrid", title="Masters Madrid, 2024", intro="The first international event of the 2024 season, arriving in a new host city.",
             pieces=[dict(id="hello-madrid", kicker="At Edelman", title="Hello, Madrid",
                          text=["A journey into the host city that lands on the Masters Madrid reveal, announcing that VALORANT's international stage has "
                                "arrived. Madrid itself became a character, connecting the EMEA league to the international stage so fans felt the jump in "
                                "stakes, with the film cut and sequenced for each platform in the run-up to the event."],
                          role="Creative direction: setting the creative vision, briefing and guiding the production team, reviewing cuts against the brief "
                               "and making sure the finished film was built to perform on social.",
                          media=[[("v", "masters-madrid-hello", "Hello Madrid: VALORANT Masters Madrid 2024")]])]),
    ],
    related=[("vct-emea-2024", "VCT EMEA 2024"), ("vct-emea-2023", "VCT EMEA 2023")],
    skills=["Campaign strategy", "Localisation", "Cultural insight", "Creative direction", "Cross-office collaboration", "Event marketing"],
    media={},
))

P.append(dict(
    slug="vct-emea-2024", featured=True,
    title="VCT EMEA 2024", client="Riot Games", via="At Edelman", year="2024–25",
    platforms="YouTube, X, Instagram, TikTok", cat="League season, year two",
    thumb=("grid", ["vct24-kickoff-teaser", "love-what-you-do-mimi", "frenzy-fire-blind-rankings", "vct24-splashx"]), hero=("v", "vct24-kickoff-teaser"),
    quote="New meta. New faces. New ambitions.",
    summary="Year two of VALORANT's EMEA partnership league, and its biggest year so far. At Edelman I owned the creative and content pipeline "
            "for the season: the films that opened, restarted and closed it, and the always-on content that carried it.",
    challenge=["Year two of a partnership league has a different job from year one. 2024 brought a new Kickoff tournament, a new team promoted through "
               "Ascension and a season split into stages: each chapter needed its own reason to tune in, and returning fans needed new reasons to stay "
               "between the tentpoles."],
    role=[ED],
    approach=["Make every chapter an event, and keep what fans came back for:",
              ("steps", [("Find the story of the moment", "Kickoff is about change, Stage 2 about a new look and new stakes, the Grand Finals about legacy."),
                         ("Give each chapter its own creative world", "New visual language and tone each time, built on the league's new 2024 brand."),
                         ("Refresh, don't repeat", "The strongest 2023 formats returned with new mechanics, so returning fans got something new."),
                         ("Go deeper on players", "Documentary content, measured on sentiment and engagement rather than raw reach."),
                         ("Cut natively, then iterate", "Bespoke edits for every platform; read reach, engagement and sentiment and carry the learnings into the next chapter.")])],
    idea=None,
    results=[("1M+", "Views, Kickoff teaser", "15K+ engagements"), ("600K+", "Reach, Stage 2 teaser", "7K engagements"),
             ("99%+", "Positive sentiment", "Meet the Player"), ("+25%", "Views and engagement, Frenzy Fire", "vs 2023")],
    results_note="", delivered=[],
    chapters=[
        dict(id="teasers", title="Season teasers", intro="The films that opened, restarted and closed the season, each built around what was new at that point.",
             pieces=[dict(id="season-teasers", kicker="Tentpole campaign films", title="Kickoff, Stage 2 and the Grand Finals",
                          text=[("h", "New meta, new faces, new ambitions"),
                                "The Kickoff teaser introduced the new tournament, the new team and the stakes of a new season.",
                                ("h", "You are not ready"),
                                "An abstract Stage 2 teaser in a new style, built on the league's new brand colours and imagery.",
                                ("h", "Grand Finals"),
                                "A finals teaser for the league's biggest year, and the best-performing finals teaser the league had run. The 2024 Grand Finals "
                                "became the most-watched EMEA Grand Finals in VALORANT history."],
                          role="I led creative development and campaign planning: writing and shaping the creative briefs, working with video studio "
                               "partners from concept to final cut, aligning Riot's product, brand and game teams, and building the cross-platform rollout.",
                          stats=[("1M+", "Views, Kickoff teaser", "15K+ engagements across platforms"), ("600K+", "Reach, Stage 2 teaser", "7K engagements"),
                                 ("160K+", "Concurrent viewers", "2024 Grand Finals, the event itself")],
                          note="The concurrent-viewer figure is for the event itself, across Twitch and YouTube, and is shown for context.",
                          media=[[("v", "vct24-kickoff-teaser", "2024 Kickoff teaser: New meta, new faces, new ambitions")],
                                 [("v", "vct24-stage2-teaser", "Stage 2 teaser: You are not ready"), ("v", "vct24-grand-finals-teaser", "2024 Grand Finals teaser")]])],
             compact_label="Also in the season",
             compact=[("Bringing the Pressure with SplashX", "vct24-splashx", "v",
                       "A joint project with Riot's brand and game teams: an 80s-style water-gun film starring our talent, promoting the new SplashX skin bundle.", "", "splashx"),
                      ("2025 Kickoff: Take What's Yours", "vct25-kickoff-teaser", "v",
                       "The teaser for the 2025 season opener. My role: creative input and social campaign planning.", "", "kickoff-2025")]),
        dict(id="always-on", title="Always-on content", intro="The formats fans came back for, refreshed for a second season, and a new way to meet the players.",
             pieces=[dict(id="meet-the-player", kicker="Player documentary series", title="Meet the Player",
                          text=["A series of mini-documentaries about players' lives in and outside VALORANT: the ups and downs of a career, told at home. "
                                "It started with G2's Mimi in her hometown in Denmark. Documentary content builds affinity rather than raw reach, so sentiment "
                                "and engagement were the KPIs."],
                          role="I helped select the players worth featuring, shaped the editorial angle for each film, supported the on-location production "
                               "and set the measurement framework, putting sentiment and engagement ahead of reach.",
                          stats=[("99%+", "Positive sentiment"), ("8,000+", "Engagements across the four films")],
                          media=[[("v", "love-what-you-do-mimi", "Meet the Player: G2 Mimi")]]),
                     dict(id="frenzy-fire-2024", kicker="Quiz series, season two", title="Frenzy Fire",
                          text=["The league's quiz format returned with new mechanics, including He Said That?, where players guess which pro said a given "
                                "quote, and Blind Rankings."],
                          role="I carried the series forward at Edelman, evolving the format and tracking its year-on-year growth.",
                          stats=[("+25%", "Views and engagement", "vs the 2023 series")],
                          media=[[("v", "frenzy-fire-blind-rankings", "Frenzy Fire: Blind Rankings"), ("v", "frenzy-fire-2024", "Frenzy Fire: He Said That?")]])],
             compact_label="Also in the season",
             compact=[("Run It Back", "run-it-back-amy", "v",
                       "The play-analysis series continued into 2024. Episode four: Amy, VCT Game Changers EMEA.", "", "run-it-back")],
             related_label="Also from 2024", related=[("push-to-talk", "Push to Talk × Logitech G"), ("vct-emea-tiktok-launch", "VCT EMEA on TikTok")]),
    ],
    related=[("valorant-masters", "VALORANT Masters"), ("vct-emea-2023", "VCT EMEA 2023")],
    skills=["Creative direction", "Campaign platforming", "Documentary storytelling", "Series development", "Multi-platform distribution", "Video production"],
    media={},
))

P.append(dict(
    slug="vct-emea-2023", featured=True,
    title="VCT EMEA 2023", client="Riot Games", via="In-house", year="2023",
    platforms="YouTube, X, Instagram, TikTok · IRL", cat="League launch year",
    thumb=("grid", ["join-us", "unlocked-fnatic", "showstopper", "gekko-5"]), hero=("i", "join-us-still-1"),
    quote="A new league, introduced by its players.",
    summary="VALORANT's EMEA partnership league launched in 2023, with ten partner teams and a new studio in Berlin. In-house at Riot Games I owned "
            "the social and creative strategy for its first season: the launch, the always-on content that carried it, and the work that brought fans to Berlin.",
    challenge=["2023 was a new structure for VALORANT esports in EMEA: ten partner teams, a new studio in Berlin and a season that ran for months. Fans "
               "needed a reason to commit to a league they hadn't seen yet, then reasons to keep coming back between the big moments, and to turn up in person."],
    role=[RG,
          "Across the season I set the social and creative strategy and led delivery: briefing and managing agencies and production vendors, building "
          "content calendars, running the influencer programme with creators on the ground in the studio, and reporting performance to optimise the mix."],
    approach=["Win fans at launch, then give every kind of fan a reason to stay:",
              ("steps", [("Lead with the players", "Personalities sell a new league faster than logos and formats do."),
                         ("Grow every team's fandom", "Give each partner team its own platform, so no fanbase is left out."),
                         ("A format for every kind of fan", "Rivalries for the competitive, nostalgia for long-time fans, personality for new ones, creators to bring the league to their own communities."),
                         ("Set a rhythm", "Weekly series between the tentpoles, so the channels never go quiet."),
                         ("Bring it into the room", "Paid and experiential work that turned viewers into visitors at the Berlin studio."),
                         ("Optimise the mix", "Track each format and put more behind what's working.")])],
    idea=None,
    results=[("1M", "Views, Join Us", "10K+ engagements"), ("~600K", "Views, Unlocked", "~40K engagements"),
             ("1M+", "Reach through the influencer programme", ""), ("~10%", "Conversion on ticket-link clicks", "Lock Your Tickets")],
    results_note="", delivered=[],
    chapters=[
        dict(id="launch", title="Launch and teasers", intro="Introducing a new league, its ten teams and its biggest moments.",
             pieces=[dict(id="join-us", kicker="League launch", title="Join Us",
                          text=["The launch film for the first season of the partnership league: players in everyday Berlin, the league's new home, each with "
                                "a character beat, inviting fans into the new league rather than announcing it at them. Photography from the same shoot fed "
                                "launch-week posts and always-on content, and a cinematic opening teaser followed on the eve of the season."],
                          role="I set the social and creative strategy, worked with the creative and production teams on the concept and shoot, planned the "
                               "content calendar and rollout across channels, and owned performance tracking after launch.",
                          stats=[("1M", "Views, Join Us", "10K+ engagements"), ("100K", "Views, opening teaser", "3K engagements")],
                          media=[[("v", "join-us", "Join Us")],
                                 [("i", "join-us-still-1", "Players photographed for Join Us"), ("i", "join-us-still-0", "Players photographed for Join Us")],
                                 [("i", "join-us-still-2", "Players photographed for Join Us"), ("i", "join-us-still-3", "Players photographed for Join Us")],
                                 [("v", "vct23-opening-teaser", "VCT EMEA 2023 opening teaser")]]),
                     dict(id="unlocked", kicker="Long-form documentary series", title="Unlocked",
                          text=["A ten-episode documentary series, one per partner team, filmed in each team's hometown and headquarters ahead of the league "
                                "launch. The players talk about their motivations, their goals and what they're excited about this season, so fans had "
                                "reasons to pick a side before the first match. Likely the most popular series on the VCT EMEA YouTube channel to date."],
                          role="I owned the series as part of the launch: defining the format and editorial angle, coordinating with the ten partner teams, "
                               "working with production on the shoots and edits, and planning the YouTube release schedule and social cut-downs.",
                          stats=[("~600K", "Total views"), ("~40K", "Engagements")],
                          media=[[("v", "unlocked-fnatic", "Unlocked, episode one: Fnatic")]])],
             compact_label="Also in the season",
             compact=[("What We're Made Of", "vct23-playoffs-teaser", "v", "The teaser for the VCT EMEA 2023 Playoffs.", "", "playoffs-teaser"),
                      ("Ascension promo", "ascension-promo", "v",
                       "A highly abstract promo for Ascension, where tier 2 teams compete for a place in the league. I co-created it with a Madrid-based studio.",
                       "50K reach · 2K engagements", "ascension"),
                      ("Game Changers EMEA promo", "game-changers-promo", "v",
                       "Promo film for VCT Game Changers EMEA 2023. My role: creative input and social campaign planning.", "", "game-changers")]),
        dict(id="always-on", title="Always-on content", intro="The series and programmes that carried the season between the tentpoles, with a format for every kind of fan.",
             pieces=[dict(id="frenzy-fire", kicker="Quiz series", title="Frenzy Fire",
                          text=["A quick-fire quiz series that tests VCT EMEA pros on their own game and league: bold graphics, a scoreboard and players who "
                                "really want to win. The same format scaled across the whole league every week, and every round was built to clip for "
                                "Shorts, Reels, TikTok and X. It became one of the league's most popular formats, and returned in 2024."],
                          role="I owned the format's place in the content strategy, planned the question sets and player line-ups with production, and "
                               "managed publishing and cut-downs across platforms.",
                          stats=[("500K", "Views, 2023 series", "7 videos"), ("70K", "Engagements, 2023 series")],
                          media=[[("v", "frenzy-fire-2023", "Frenzy Fire, 2023")]])],
             compact_label="The rest of the slate",
             compact=[("Showstopper", "showstopper", "v",
                       "Two-to-three-minute films about the rivalries between regions, countries and teams, promoting each week's broadcast.",
                       "260K views · ~7K engagements", "showstopper"),
                      ("Run It Back", "run-it-back-aslan", "v",
                       "A play-analysis series with VCT EMEA and VCT Game Changers EMEA players, which continued into 2024. Episode one: AsLanM4shadow.",
                       "30K views · 1K engagements across five videos, 2023–24", "run-it-back"),
                      ("First Champs", "first-champs", "v",
                       "Reuniting the first-ever VCT champions, from EMEA, in a piece of league history fans could rally behind.", "40K reach · 2K engagements", "first-champs"),
                      ("Do It Yourself", "do-it-yourself", "v", "A three-episode series.", "100K views · ~8K engagements", "do-it-yourself"),
                      ("Talent announcement", "talent-announcement", "v",
                       "An unconventional talent announcement: a video instead of a static graphic, crossing over with the League of Legends LEC studio and talent.",
                       "~10K reach · ~700 engagements, above average for this kind of announcement", "talent-announcement"),
                      ("Admission forms", "admission-form", "i",
                       "Players filled in admission forms with personal facts and quirky drawings, inspired by how Formula 1 and other top sports present athletes.",
                       "~100K reach · ~6K engagements", "admission-forms"),
                      ("Influencer watch parties", "influencer-watch-parties", "i",
                       "Weekly watch parties hosted by creators, plus on-the-ground content with them in the studio.", "1M+ reach across hundreds of influencers", "watch-parties")],
             partners_label="2023 partners", partners=["Logitech G", "Aim Lab", "Cougar", "Red Bull"],
             related_label="Also from 2023", related=[("push-to-talk", "Push to Talk × Logitech G")]),
        dict(id="berlin", title="Bringing fans to Berlin", intro="Paid and experiential work for the league's new home at Messe Berlin.",
             pieces=[dict(id="lock-your-tickets", kicker="Paid ticketing campaign", title="Lock Your Tickets",
                          text=["A paid and organic campaign to sell tickets for the new studio, built from the ground up at Messe Berlin: a brand-new venue "
                                "with no track record, and an audience used to watching online. A fast, red-drenched trailer made the live room feel like the "
                                "place the season happens. Paid social reached in-market fans beyond the organic audience, and UTMs on every link meant spend "
                                "and messaging could shift towards what was actually selling tickets."],
                          role="I owned the social campaign: the creative brief for the trailer, the organic rollout, and the paid set-up with our media "
                               "partners, with UTM tracking on every link so ticket clicks and purchases could be attributed back to the creative.",
                          stats=[("~600K", "Views"), ("~10%", "Conversion rate on UTM clicks"), ("527.2K", "Views on the launch post on X")],
                          media=[[("v", "lock-your-tickets", "Lock Your Tickets trailer"),
                                  ("i", "lock-tickets-tweet", "Launch post on X: Watch your favourite VCT EMEA team live at our Coliseum in Berlin Messe")]]),
                     dict(id="gekko", kicker="Experiential", title="Gekko's bubble tea truck and the fan wall",
                          text=["A VALORANT-branded bubble tea truck themed on the agent Gekko, part of a wider 2023 out-of-home campaign. It was parked near "
                                "Alexanderplatz in Berlin for three weekends only, then came into the studio, where visitors used the tokens they got on entry "
                                "to redeem a free drink. It was one of the most popular activations of the year, and fans asked for it to come back.",
                                "Alongside it, a VCT EMEA-branded wall at the Coliseum where fans could sign their names and leave their mark on the league's history."],
                          role="I managed the social side of the truck end to end: the content plan, capture on site, community engagement and reporting on "
                               "sentiment and reach. The fan wall was my idea, planned from the start as both a social moment and a piece of VCT EMEA history.",
                          stats=[("2,000+", "Free bubble teas served")],
                          media=[[("i", "gekko-5", "Gekko's bubble tea truck in Berlin"), ("i", "gekko-9", "The truck in the VCT EMEA studio")],
                                 [("i", "gekko-6", "Serving bubble tea from the truck"), ("i", "gekko-3", "VALORANT-themed bubble tea"), ("i", "gekko-8", "Gekko artwork on the truck")],
                                 [("i", "gekko-tweet", "VALORANT Esports EMEA post on X about the Gekko truck"), ("i", "fan-wall", "The signed VCT EMEA fan wall"),
                                  ("i", "fan-wall-tweet", "VALORANT Esports EMEA post on X about the fan wall")]])],
             related_label="Also from 2023", related=[("vct-emea-bootcamp", "VCT EMEA Bootcamp"), ("valorant-masters", "VALORANT Masters Tokyo")]),
    ],
    related=[("vct-emea-2024", "VCT EMEA 2024"), ("valorant-masters", "VALORANT Masters")],
    skills=["Content strategy", "Campaign launch", "Long-form content", "Paid social", "Experiential", "Influencer marketing", "Agency and vendor management"],
    media={},
))

# Order the Work page and carousel: Google Cloud, then VALORANT Esports (hubs and standalone campaigns), then G2 and independent work.
_ORDER = ["google-cloud-london-summit", "the-fa-x-google-cloud", "luminary-programme", "valorant-masters", "vct-emea-2024", "vct-emea-tiktok-launch",
          "vct-emea-2023", "push-to-talk", "vct-emea-bootcamp", "g2-esports-x-adidas", "pink-pony-streamathon", "origin-and-the-creator-years"]
P.sort(key=lambda d: _ORDER.index(d["slug"]))


# One-line overview shown under the title and labels on work cards. Each is a
# condensed version of the project's own summary above, so no new claims.
LINES = {
    "valorant-masters": "Anime-style art and Japanese-localised coverage for Tokyo, and a Madrid hype film.",
    "vct-emea-2024": "Year two at Edelman: season teasers, player documentaries and always-on series.",
    "vct-emea-2023": "The launch year of VALORANT's EMEA league: films, series and fan moments in Berlin.",
    "google-cloud-london-summit": "Social coverage that kept Google Cloud's London Summit working after the keynote.",
    "the-fa-x-google-cloud": "A vertical video series putting England players up against Google Cloud's AI tools.",
    "luminary-programme": "An always-on LinkedIn programme keeping Google Cloud's leaders visible and credible.",
    "vct-emea-2024-season-teasers": "The films that opened, restarted and closed VALORANT's EMEA league in 2024.",
    "valorant-masters-madrid": "Creative direction for the hype campaign around VALORANT's first 2024 international.",
    "vct-emea-tiktok-launch": "Launching VCT EMEA on TikTok with native content: 100,000 followers in a year.",
    "meet-the-player": "Mini-documentaries about players' lives in and outside VALORANT.",
    "join-us-vct-emea-2023": "The launch films for the first season of VALORANT's partnership league in EMEA.",
    "unlocked": "A documentary series following the ten partner teams through their hometowns.",
    "push-to-talk": "A Logitech G series that lets fans hear players talk in and out of the game.",
    "frenzy-fire": "A quick-fire quiz series testing VCT EMEA pros on their own game and league.",
    "lock-your-tickets": "A paid and organic campaign to sell tickets for VCT EMEA's new studio in Berlin.",
    "vct-emea-bootcamp": "A personalised fan experience turning each player's VALORANT data into a video.",
    "gekko-truck-and-fan-wall": "Two in-person moments for fans in Berlin: a bubble tea truck and a signed fan wall.",
    "vct-emea-2023-content-slate": "The always-on content that carried VCT EMEA through its first partnership season.",
    "vct-emea-2024-content-slate": "The always-on content that carried VCT EMEA through its second year of partnership.",
    "valorant-masters-tokyo": "Anime-style team art and Japanese-localised coverage for VALORANT Masters Tokyo.",
    "run-it-back": "A play-analysis series with VCT EMEA and Game Changers EMEA players.",
    "g2-esports-x-adidas": "The social launch of adidas as G2 Esports' official apparel partner.",
    "pink-pony-streamathon": "A three-hour live charity stream from Berlin supporting young people with cancer.",
    "origin-and-the-creator-years": "Twelve years of making my own content, from gaming montages to full-time streaming.",
}
for _p in P:
    _p["line"] = LINES[_p["slug"]]
