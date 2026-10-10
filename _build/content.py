"""
Portfolio content. Every figure here comes from the campaign notes, the
CV, or on-screen data in the supplied assets. See _build/SOURCES.md for the
source of each number. Nothing is estimated.

Media references:
  ("v", "name")            -> assets/media/name.mp4 + name.webp poster
  ("i", "name", "alt")     -> assets/img/work/name.webp
Each media group is a row; items sit side by side at equal height with no cropping.
"""

EMAIL = "redacted@example.com"
LINKEDIN = ""  # TODO: paste your LinkedIn profile URL here; the link is hidden while empty

# --------------------------------------------------------------------------- positioning
HOME_INTRO = (
    "Social creative lead. I set the strategy, develop the idea, direct the content "
    "and read how it performs. Organic social at the core, paid where it scales, "
    "across culture, esports and B2B technology."
)

ABOUT_LEDE = (
    "I lead social-first creative work: the strategy behind it, the idea at the centre of it, "
    "the content that carries it, and the numbers that show whether it worked."
)

ABOUT_BODY = [
    "I spent twelve years building my own audience as a creator before I ran social for anyone else. "
    "Since then I've led social for G2 Esports, set the EMEA social and creative strategy for VALORANT Esports "
    "at Riot Games, and carried that work on at Edelman across nine markets.",
    "Today I'm Social Content Manager at Jellyfish, where I lead social content on the Google Cloud account: "
    "turning complex technology into content that executives, engineers and broader audiences actually stop for, "
    "and running the Luminary Programme, which keeps Google Cloud leaders visible on LinkedIn.",
    "The through-line is the same in B2B and B2C. Find the cultural moment a brand has a right to be in, build one idea "
    "strong enough to travel across platforms and markets, make each version feel native to where it lands, "
    "then measure honestly and make the next one better.",
]

SERVICES = [
    ("Social strategy", "london-summit-sizzle",
     ["Channel and platform strategy", "Owned, earned and paid planning", "Audience and cultural insight", "KPIs, reporting and optimisation"],
     "London Summit · VCT EMEA"),
    ("Creative direction", "vct24-kickoff-teaser",
     ["Campaign platforms and hero ideas", "Briefing agencies and studios", "Shoot direction and production", "Quality bar across every cut"],
     "Season teasers · Push to Talk"),
    ("Content and formats", "frenzy-fire-2023",
     ["Always-on series and franchises", "Short-form and vertical video", "Talent and player-led content", "Platform launches"],
     "Frenzy Fire · TikTok launch"),
    ("Executives and communities", "london-summit-alex-rutter",
     ["Executive social programmes", "Employee advocacy", "Influencer and creator programmes", "Live and IRL fan moments"],
     "Luminary · Influencer watch parties"),
]

STATS = [  # (number, suffix, label) – all verified in SOURCES.md
    (15, "+", "Years in social, content and community"),
    (4.1, "M", "Earned impressions, Google Cloud London Summit 2026"),
    (100, "K", "TikTok followers in VCT EMEA's first year on the platform"),
    (2021, "", "Esports Creative Piece of the Year, G2 Esports × adidas"),
]

EXPERIENCE = [
    ("Jellyfish", "Social Content Manager, on the Google Cloud account", "2025–now", "london-summit-sizzle"),
    ("Edelman", "Social & Content Lead, on the Riot Games account", "2024–25", "vct24-kickoff-teaser"),
    ("Riot Games", "Social Media Strategist, EMEA · VALORANT Esports", "2022–24", "join-us"),
    ("G2 Esports", "Social Media Manager", "2020–22", "g2-adidas-film"),
    ("Independent", "Content Creator & Consultant", "2008–20", "origin"),
]

BRANDS = ["Google Cloud", "The FA", "Riot Games", "VALORANT Esports", "adidas", "Ralph Lauren", "Logitech G",
          "Red Bull", "Aim Lab", "Cougar", "Paysafecard", "Unilumin", "OMEN by HP", "Intel", "Snickers"]

# --------------------------------------------------------------------------- case studies
# via: how Ramtin was involved: employer or agency, so client and employer are never confused
P = []

P.append(dict(
    slug="google-cloud-london-summit", featured=True,
    title="London Summit 2026", client="Google Cloud", via="At Jellyfish", year="2026",
    platforms="LinkedIn, X, Instagram, Facebook", cat="B2B event campaign",
    thumb=("frame", "london-summit-sizzle", 21), quote="From live event to week-long conversation.",
    summary="An earned and owned social campaign built to make Google Cloud's London Summit the UK's reference point for AI and data cloud, "
            "and to make the day's content keep working long after the keynote ended.",
    challenge=["The brief was explicit: establish Google Cloud as the leading authority in AI and data cloud in the UK market. "
               "Every major cloud provider was making that claim, to the same audience of technical and business decision-makers.",
               "Event content usually peaks on the day and disappears. The challenge was to turn one summit into authority that "
               "showed up in owned channels, in people's own feeds, and in trade media."],
    role=["As Social Content Lead on the Google Cloud account at Jellyfish, I owned the Summit's social content from brief through to execution, "
          "working with the Google Cloud team, Jellyfish strategists and production partners."],
    approach=["We split the job into three layers, each with its own purpose and measure:",
              ("list", ["<strong>Owned, to build authority.</strong> LinkedIn, X, Instagram and Facebook, measured on weighted engagement.",
                        "<strong>Earned, to build trust.</strong> Halo (Google Cloud's employee advocacy platform), influencers and the executives in the Luminary Programme, measured on share of voice and reach.",
                        "<strong>Paid, to build scale.</strong> TechTarget and Condé Nast, measured on impressions and sentiment."]),
              "That structure meant the same moment from the stage could appear as a brand post, an executive's own LinkedIn update, an employee share and a paid placement, each doing a different job."],
    idea=["Treat the Summit as a content studio, not just a stage. Executives, speakers and Gemini masterclass sessions were captured on the day "
          "as platform-native video and stories, then distributed through every layer above. The campaign's own line put it simply: "
          "don't just capture your event, scale it."],
    delivered=["Owned, earned and paid channel strategy with a KPI per layer",
               "Executive monologue video filmed at the Summit",
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
           "after_approach": [("v", "london-summit-alex-rutter", "Executive monologue filmed at the Summit: Alex Rutter, EMEA Managing Director, AI, Google Cloud")]},
))

P.append(dict(
    slug="the-fa-x-google-cloud", featured=True,
    title="The FA × Google Cloud", client="The FA · Google Cloud", via="At Jellyfish", year=None,
    platforms="Vertical social video (9:16)", cat="Partnership content",
    thumb=("composite", ["fa-roboball", "fa-creative-agent", "fa-get-to-know"]), quote="Robot football, powered by Gemini.",
    summary="A vertical video series that put England players in front of Google Cloud's AI tools, so football fans could see what Gemini does by watching players compete with it.",
    challenge=["AI products are abstract, and sports partnership content often ends up as players standing next to a logo. "
               "This had to engage a football audience in a conversation about AI, and feel high-energy and playful rather than like a product demo."],
    role=["Social Content Lead on the Google Cloud account at Jellyfish. I was part of the team that developed the hero concepts below, "
          "with responsibility for how they would play on social and for carrying the series through to delivery."],
    approach=["Lead with play, not product. Each format turns one Gemini capability into a game the players genuinely want to win, "
              "so the technology is understood by watching it work.",
              "Two hero films carry the product story. Lighter quick-fire formats keep the players' personalities front and centre "
              "and give the series frequency between the bigger pieces."],
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
    role=["I lead the programme end to end at Jellyfish: planning, content, executive relationships and publishing."],
    approach=[("list", ["<strong>Zero self-briefing.</strong> Executives don't have to come up with ideas or write anything. The programme brings them ready-to-publish content in their own voice.",
                        "<strong>Aligned to the business calendar.</strong> Product launches, priority company announcements, customer stories, partner milestones, regional news and key field and industry events.",
                        "<strong>Native publishing.</strong> Posts go out from the executives' own profiles, managed by Jellyfish in Sprinklr with the right permissions, scheduling and milestones in place.",
                        "<strong>Adoption over output.</strong> Success means published and adopted, not just produced."])],
    idea=["One moment, many credible voices. Around a launch like Gemini at Work '26, each executive takes the angle that fits their remit: "
          "productivity for the UK, Ireland and Sub-Saharan Africa CEO, financial services for the EMEA AI lead, engineering, security and digital sovereignty for others. "
          "The audience gets five different reasons to care instead of one press release repeated five times."],
    delivered=["Always-on executive content calendar", "Post copy and creative tailored to each executive",
               "Native publishing on executives' own profiles via Sprinklr", "Coordination with each executive's point of contact",
               "Amplification of launches, customer stories, partner milestones and regional moments"],
    results=[],
    results_note="Programme metrics weren't included in the supplied material. The evidence shown is the published work: coordinated posts from five Google Cloud executives around Gemini at Work '26.",
    skills=["Executive social", "Thought leadership", "B2B LinkedIn", "Programme management", "Stakeholder management", "Sprinklr"],
    media={"hero": [("i", "luminary-1", "LinkedIn post by Maureen Costello, Google Cloud, about Gemini at Work"),
                    ("i", "luminary-4", "LinkedIn post by Alex Rutter, Google Cloud, about Lloyds Banking Group and Gemini Enterprise"),
                    ("i", "luminary-2", "LinkedIn post by Chris Lindsay, Google Cloud, about Merck and Gemini Enterprise")],
           "after_approach": [("i", "luminary-3", "LinkedIn post by Dr. Marianne Janik, Google Cloud, about digital sovereignty"),
                              ("i", "luminary-5", "LinkedIn post by Ben Cabanas, Google Cloud, about Gemini agent")],
           "extra_title": "More executive-led video from the Google Cloud account",
           "extra_note": "Not part of the Luminary Programme case study above. Shown here as further examples of executive-fronted content on the account.",
           "extra": [("v", "exec-maureen-drone-challenge", "Maureen Costello on drone technology and supply chains"),
                     ("v", "exec-daniel-walker-murray", "Daniel Walker-Murray on Gemini Enterprise"),
                     ("v", "exec-joana-deepmind", "Joana Carrasqueira, Google DeepMind, on vibe coding")]},
))

P.append(dict(
    slug="vct-emea-2024-season-teasers", featured=True,
    title="VCT EMEA 2024: Season Teasers", client="Riot Games", via="At Edelman", year="2024",
    platforms="YouTube, X, Instagram, TikTok", cat="Tentpole campaign films",
    thumb=("v", "vct24-kickoff-teaser"), quote="New meta. New faces. New ambitions.",
    summary="The films that opened, restarted and closed VALORANT's EMEA league in its biggest year so far, each built around what was new at that point in the season.",
    challenge=["2024 brought a new Kickoff tournament, a new team promoted through Ascension, and a season split into stages. "
               "Each stage needed its own reason to tune in, without repeating the same hype formula the audience had already seen."],
    role=["Social & Content Lead on the Riot Games account at Edelman, leading creative development across YouTube, X, Instagram and TikTok "
          "and working with video studio partners on the teasers."],
    approach=["Treat each teaser as a chapter with its own story, not a reskin of the last one. Kickoff was about change, Stage 2 introduced a new visual language, "
              "and the Grand Finals teaser had one job: make the biggest weekend of the year feel unmissable.",
              "Every film was cut for each platform rather than posted once and shared everywhere."],
    idea=[("h", "New meta, new faces, new ambitions"),
          "The Kickoff teaser introduced the new tournament, the new team and the stakes of a new season.",
          ("h", "You are not ready"),
          "An abstract Stage 2 teaser in a new style, built on the league's new brand colours and imagery.",
          ("h", "Grand Finals"),
          "A finals teaser for the league's biggest year.",
          ("h", "Bringing the Pressure with SplashX"),
          "A joint project with Riot's brand and game teams: an 80s-style water-gun film starring our talent, promoting the new SplashX skin bundle."],
    delivered=["2024 Kickoff teaser", "Stage 2 teaser", "Grand Finals teaser", "SplashX skin bundle film", "2025 Kickoff teaser, Take What's Yours"],
    results=[("1M+", "Views, Kickoff teaser", "15K+ engagements across platforms"),
             ("600K+", "Reach, Stage 2 teaser", "7K engagements"),
             ("160K+", "Concurrent viewers", "2024 Grand Finals, the most-watched EMEA Grand Finals in VALORANT history")],
    results_note="The Grand Finals teaser was the best-performing finals teaser the league had run. The concurrent-viewer figure is for the event itself, across Twitch and YouTube, and is shown for context.",
    skills=["Creative direction", "Campaign platforming", "Brand storytelling", "Video production", "Multi-platform distribution"],
    media={"hero": [("v", "vct24-kickoff-teaser", "2024 Kickoff teaser: New meta, new faces, new ambitions")],
           "after_approach": [("v", "vct24-stage2-teaser", "Stage 2 teaser: You are not ready"), ("v", "vct24-grand-finals-teaser", "2024 Grand Finals teaser")],
           "after_delivered": [("v", "vct24-splashx", "Bringing the Pressure with SplashX"), ("v", "vct25-kickoff-teaser", "2025 Kickoff teaser: Take What's Yours")]},
))

P.append(dict(
    slug="vct-emea-tiktok-launch", featured=True,
    title="VCT EMEA on TikTok", client="Riot Games", via="At Edelman", year="2024",
    platforms="TikTok", cat="Platform launch",
    thumb=("composite", ["tiktok-clip-1", "tiktok-clip-2"]), quote="Zero to 100K in year one.",
    summary="The launch of VCT EMEA's TikTok channel, built on native content captured with players and talent, which grew to 100,000 followers in its first year.",
    challenge=["A new channel starts at zero, and TikTok audiences scroll past anything that looks like a repurposed broadcast clip. "
               "Player time is limited across a season, so native content had to be planned rather than hoped for."],
    role=["I was responsible for the TikTok launch campaign for social."],
    approach=["Use media day, when the league captures its evergreen content for the year, to also capture TikTok-native shorts. "
              "One access window with the players and talent produced a bank of content written for the platform from the start."],
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
    slug="love-what-you-do", featured=False,
    title="Love What You Do", client="Riot Games", via="At Edelman", year="2024",
    platforms="YouTube, X, Instagram", cat="Player documentary series",
    thumb=("v", "love-what-you-do-mimi"), quote="Players, at home.",
    summary="A series of mini-documentaries about players' lives in and outside VALORANT, starting with G2's Mimi in her hometown in Denmark.",
    challenge=["Fans know players through their gameplay, not as people. Reach-led formats grow numbers but rarely build lasting fandom for individual players."],
    role=["Social & Content Lead on the Riot Games account at Edelman. We chose the players to feature deliberately, and I helped shape the series and its measurement."],
    approach=["Choose a small number of players worth knowing better, go to where they're from, and judge the series on the right metric. "
              "Documentary pieces tend to engage deeply rather than reach widely, so sentiment and engagement were the KPIs, not views."],
    idea=["Love What You Do: the ups and downs of a career, inside the game and outside it, told at home. For Mimi, that meant filming in her hometown in Denmark."],
    delivered=["Four player feature films", "On-location shoot in Denmark for the Mimi episode", "Social cutdowns and distribution"],
    results=[("99%+", "Positive sentiment", ""), ("8,000+", "Engagements across the four films", "")],
    results_note="",
    skills=["Documentary storytelling", "Talent development", "Sentiment-led measurement", "Video production"],
    media={"hero": [("v", "love-what-you-do-mimi", "Love What You Do: G2 Mimi")]},
))

P.append(dict(
    slug="join-us-vct-emea-2023", featured=True,
    title="Join Us: VCT EMEA 2023", client="Riot Games", via="In-house", year="2023",
    platforms="YouTube, X, Instagram, TikTok", cat="League launch",
    thumb=("i", "join-us-still-1"), quote="A new league, introduced by its players.",
    summary="The launch films for the 2023 season of VCT EMEA, the first year of VALORANT's partnership league: Join Us, and the opening teaser.",
    challenge=["2023 was a new structure for VALORANT esports in EMEA, with ten partner teams and a new studio in Berlin. "
               "Fans needed a reason to commit to a league they hadn't seen yet."],
    role=["As Social Media Strategist for EMEA at Riot Games, I set the social and creative strategy for the launch and directed the campaign across channels."],
    approach=["Launch with people, not logos. Put the players in ordinary places around the city and let their personalities sell the league, "
              "then follow with a cinematic opening teaser on the eve of the season."],
    idea=["Join Us: players in everyday Berlin, each with a character beat, inviting fans into the new league rather than announcing it at them."],
    delivered=["Join Us launch film", "Photography from the Join Us shoot", "VCT EMEA 2023 opening teaser"],
    results=[("1M", "Views, Join Us", "10K+ engagements"), ("100K", "Views, opening teaser", "3K engagements")],
    results_note="",
    skills=["Campaign launch", "Creative direction", "Talent-led content", "Photography direction"],
    media={"hero": [("v", "join-us", "Join Us")],
           "after_approach": [("i", "join-us-still-1", "Players photographed for Join Us"), ("i", "join-us-still-0", "Players photographed for Join Us")],
           "after_idea": [("i", "join-us-still-2", "Players photographed for Join Us"), ("i", "join-us-still-3", "Players photographed for Join Us")],
           "after_delivered": [("v", "vct23-opening-teaser", "VCT EMEA 2023 opening teaser")]},
))

P.append(dict(
    slug="unlocked", featured=True,
    title="Unlocked", client="Riot Games", via="In-house", year="2023",
    platforms="YouTube", cat="Long-form documentary series",
    thumb=("v", "unlocked-fnatic"), quote="Ten teams, ten hometowns.",
    summary="A long-form documentary series that followed the ten partner teams through their hometowns ahead of the 2023 VCT EMEA launch.",
    challenge=["The league launch needed hype, but the teams were also new to a lot of the audience. Fans needed reasons to pick a side before the first match."],
    role=["Social Media Strategist for EMEA at Riot Games, responsible for the series as part of the 2023 launch campaign."],
    approach=["Make the launch about the teams' roots. A mini-documentary per partner team, released in the run-up to Kickoff, "
              "introduces the players, their motivations, goals and what they're excited about, and grows each team's fandom as well as the league's."],
    idea=["Unlock each team: go to where the organisation is from and let the players show you around."],
    delivered=["Ten-episode documentary series, one per partner team", "Episode one: Fnatic"],
    results=[("~600K", "Total views", ""), ("~40K", "Engagements", "")],
    results_note="Likely the most popular series on the VCT EMEA YouTube channel to date.",
    skills=["Long-form content", "Documentary storytelling", "Launch strategy", "YouTube"],
    media={"hero": [("v", "unlocked-fnatic", "Unlocked, episode one: Fnatic")]},
))

P.append(dict(
    slug="push-to-talk", featured=True,
    title="Push to Talk × Logitech G", client="Riot Games · Logitech G", via="In-house, then at Edelman", year="2023–24",
    platforms="YouTube, X", cat="Sponsored series",
    thumb=("v", "push-to-talk-2023"), quote="Hear the game the players hear.",
    summary="A sponsored series I created with Logitech G: mic-check content that lets fans hear players talk in and out of the game as they prepare, set up and compete.",
    challenge=["Sponsor content in esports is easy to skip. Logitech needed an integration that made sense for a headset and microphone brand "
               "and that fans would actually want to watch."],
    role=["I created the series and worked hand in hand with Logitech to build a format that fit their brand and our audience. "
          "I led it in 2023 at Riot Games and evolved it in 2024 at Edelman."],
    approach=["Start from the product's truth. Logitech makes the headsets and microphones players use, so the content should be about what you hear through them. "
              "Logitech sponsored the series and put paid support behind it."],
    idea=["Push to Talk: a mic-check format. Player comms, banter and calls during matches, cut together so fans hear the game the way the players do."],
    delivered=["Seven-episode series in 2023", "A redesigned format, structure and layout in 2024", "Paid support in partnership with Logitech"],
    results=[("300K", "Views, 2023 series", "7 episodes"), ("21K", "Engagements, 2023 series", ""), ("~50%", "Better performance in 2024", "vs the 2023 series")],
    results_note="",
    skills=["Format creation", "Brand partnerships", "Sponsor integration", "Paid and organic", "Series development"],
    media={"hero": [("v", "push-to-talk-2023", "Push to Talk, 2023")],
           "after_delivered": [("v", "push-to-talk-2024", "Push to Talk, 2024 episode")]},
))

P.append(dict(
    slug="frenzy-fire", featured=True,
    title="Frenzy Fire", client="Riot Games", via="In-house, then at Edelman", year="2023–24",
    platforms="YouTube, X, Instagram, TikTok", cat="Quiz series",
    thumb=("v", "frenzy-fire-2023"), quote="How well do pros know their own game?",
    summary="A quick-fire quiz series that tests VCT EMEA pros on their own game and league, and became one of the league's most popular formats.",
    challenge=["The league needed always-on content between broadcasts that showed players' personalities, was efficient to produce, and worked in clips across platforms."],
    role=["Part of the VCT EMEA content slate I led at Riot Games in 2023, then continued and grown in 2024 at Edelman."],
    approach=["A simple, repeatable quiz format that works with any player, produces a full series and cuts down into short clips for every platform. "
              "In 2024 the format moved on, with players guessing which pro said a given quote."],
    idea=["Quick-fire questions, bold graphics, a scoreboard and players who really want to win."],
    delivered=["Seven-episode 2023 series", "2024 series, including He Said That?"],
    results=[("500K", "Views, 2023 series", "7 videos"), ("70K", "Engagements, 2023 series", ""), ("+25%", "Views and engagement in 2024", "vs 2023")],
    results_note="",
    skills=["Format creation", "Always-on content", "Talent-led content", "Short-form clipping"],
    media={"hero": [("v", "frenzy-fire-2023", "Frenzy Fire, 2023")],
           "after_delivered": [("v", "frenzy-fire-2024", "Frenzy Fire 2024: He Said That?")]},
))

P.append(dict(
    slug="lock-your-tickets", featured=True,
    title="Lock Your Tickets", client="Riot Games", via="In-house", year="2023",
    platforms="X, YouTube, Instagram · paid social", cat="Paid ticketing campaign",
    thumb=("v", "lock-your-tickets"), quote="Sell out a studio that didn't exist yet.",
    summary="A paid and organic campaign to sell tickets for VCT EMEA's new studio, built from the ground up at Messe Berlin in 2023.",
    challenge=["A brand-new venue with no track record, and an audience used to watching online. The campaign had to turn viewers into ticket buyers, and prove it."],
    role=["As Social Media Strategist for EMEA, I owned the social campaign: the trailer rollout and the paid set-up, with ticket clicks and purchases tracked through UTMs."],
    approach=["Build the trailer as a piece of hype content first, then put paid behind it with UTM tracking, so creative performance could be read against real ticket demand rather than views alone."],
    idea=["Lock Your Tickets: a fast, red-drenched trailer that makes the live room feel like the place the season happens."],
    delivered=["Ticketing trailer", "Paid social campaign with UTM tracking", "Organic launch posts"],
    results=[("~600K", "Views", ""), ("~10%", "Conversion rate on UTM clicks", ""), ("527.2K", "Views on the launch post on X", "")],
    results_note="",
    skills=["Paid social", "Performance tracking", "Conversion-led creative", "Event marketing"],
    media={"hero": [("v", "lock-your-tickets", "Lock Your Tickets trailer"), ("i", "lock-tickets-tweet", "Launch post on X: Watch your favourite VCT EMEA team live at our Coliseum in Berlin Messe")]},
))

P.append(dict(
    slug="gekko-truck-and-fan-wall", featured=True,
    title="Gekko's Bubble Tea Truck & the Fan Wall", client="Riot Games", via="In-house", year="2023",
    platforms="IRL, X, Instagram", cat="Experiential",
    thumb=("i", "gekko-5"), hero=("i", "gekko-1"), quote="Free bubble tea. Fans asked for it back.",
    summary="Two in-person moments for VALORANT fans in Berlin: Gekko's bubble tea truck, and a signed wall that made the fans part of the league's history.",
    challenge=["The studio in Berlin gave the league a physical home. The opportunity was to give fans things to do there that they'd share, and remember."],
    role=["The fan wall was my idea, planned as both a social moment and a piece of VCT EMEA history. "
          "Both activations were part of the 2023 studio experience and its social coverage."],
    approach=["IRL first, social second. Make experiences worth photographing, and the content follows."],
    idea=[("h", "Gekko's bubble tea truck"),
          "A VALORANT-branded bubble tea truck themed on the agent Gekko, for bubble tea fans and VALORANT fans alike. It first ran near Alexanderplatz in Berlin in 2021, for three weekends only. "
          "In 2023 it came into the studio, where visitors used the tokens they got on entry to redeem a free drink.",
          ("h", "The fan wall"),
          "A VCT EMEA-branded wall at the Coliseum where fans could sign their names and leave their mark on the league's history."],
    delivered=["Bubble tea truck activation in the studio, with token redemption", "Fan wall design and activation", "Social content from both"],
    results=[("2,000+", "Free bubble teas served", "")],
    results_note="The truck was measured on sentiment and reach. It was one of the most popular activations of the year, and fans asked for it to come back.",
    skills=["Experiential", "Fan engagement", "Social-first activation", "Community"],
    media={"hero": [("i", "gekko-5", "Gekko's bubble tea truck in Berlin")],
           "after_approach": [("i", "gekko-6", "Serving bubble tea from the truck"), ("i", "gekko-3", "VALORANT-themed bubble tea")],
           "after_idea": [("i", "gekko-9", "The truck in the VCT EMEA studio"), ("i", "gekko-8", "Gekko artwork on the truck"), ("i", "gekko-tweet", "VALORANT Esports EMEA post on X about the Gekko truck")],
           "after_delivered": [("i", "fan-wall", "The signed VCT EMEA fan wall")],
           "after_results": [("i", "fan-wall-tweet", "VALORANT Esports EMEA post on X about the fan wall")]},
))

P.append(dict(
    slug="vct-emea-2023-content-slate", featured=False,
    title="The 2023 Content Slate", client="Riot Games", via="In-house", year="2023",
    platforms="YouTube, X, Instagram, TikTok", cat="Always-on content",
    thumb=("v", "ascension-promo"), quote="A season's worth of reasons to watch.",
    summary="The always-on series, promos and programmes that carried VCT EMEA through its first partnership season, alongside the tentpole campaigns.",
    challenge=["A league season runs for months. Between the big moments, the channels needed a steady rhythm of content that grew fandom for teams, players and the competition itself."],
    role=["As Social Media Strategist for EMEA, I set the content strategy and led delivery across the slate, working with agencies, production vendors, influencers and broadcast talent."],
    approach=["Give every kind of fan a format: rivalries for the competitive, nostalgia for long-time fans, personality for new ones, and creators to bring the league to their own communities."],
    idea=None,
    slate=[
        ("Showstopper", "showstopper", "v", "Two-to-three-minute films about the rivalries between regions, countries and teams, promoting each week's broadcast.", "260K views · ~7K engagements"),
        ("Ascension promo", "ascension-promo", "v", "A highly abstract promo for Ascension, where tier 2 teams compete for a place in the league. I co-created it with a Madrid-based studio.", "50K reach · 2K engagements"),
        ("First Champs", "first-champs", "v", "Reuniting the first-ever VCT champions, from EMEA, in a piece of league history fans could rally behind.", "40K reach · 2K engagements"),
        ("Do It Yourself", "do-it-yourself", "v", "A three-episode series.", "100K views · ~8K engagements"),
        ("Talent announcement", "talent-announcement", "v", "An unconventional talent announcement: a video instead of a static graphic, crossing over with the League of Legends LEC studio and talent.", "~10K reach · ~700 engagements, above average for this kind of announcement"),
        ("Admission forms", "admission-form", "i", "Players filled in admission forms with personal facts and quirky drawings, inspired by how Formula 1 and other top sports present athletes.", "~100K reach · ~6K engagements"),
        ("Influencer watch parties", "influencer-watch-parties", "i", "Weekly watch parties hosted by creators, plus on-the-ground content with them in the studio.", "1M+ reach across hundreds of influencers"),
        ("VCT EMEA Bootcamp", "vct-bootcamp", "v", "A personalised video experience where fans compared themselves with VCT EMEA pros.", ""),
        ("Game Changers EMEA promo", "game-changers-promo", "v", "Promo film for VCT Game Changers EMEA 2023.", ""),
    ],
    delivered=["Showstopper rivalry series", "Ascension promo", "First Champs", "Do It Yourself series", "Talent announcement film",
               "Player admission forms", "Influencer watch party programme", "VCT EMEA Bootcamp", "Game Changers EMEA promo"],
    results=[("1M+", "Reach through the influencer programme", ""), ("260K", "Views, Showstopper", ""), ("100K", "Views, Do It Yourself", "")],
    results_note="Per-item figures are shown with each piece above.",
    partners=["Logitech G", "Aim Lab", "Cougar", "Red Bull"],
    skills=["Content strategy", "Series development", "Influencer marketing", "Agency and vendor management", "Community"],
    media={},
))

P.append(dict(
    slug="g2-esports-x-adidas", featured=True,
    title="G2 Esports × adidas", client="G2 Esports · adidas", via="In-house", year="2021",
    platforms="X, YouTube, Instagram · organic and paid", cat="Partnership launch",
    thumb=("i", "g2-adidas-newspaper"), hero=("i", "g2-adidas-shopfront"), quote="Esports Creative Piece of the Year, 2021.",
    summary="The integrated social launch of adidas as G2 Esports' official sports apparel partner, which won Esports Creative Piece of the Year in 2021.",
    challenge=["Announcing a kit partner is usually a logo lockup and a press release. adidas joining the #G2ARMY meant a pro jersey, a lifestyle collaboration and new content, "
               "and the launch had to feel as big as that, for gaming fans and sportswear fans at the same time."],
    role=["I developed the integrated social creative campaign for the launch, across organic and paid social."],
    approach=["Blend athletic and gaming-inspired creative, and tell the story natively on each platform instead of pushing one asset everywhere. "
              "Back the main film with behind-the-scenes content on YouTube and a jersey reveal for the 2021 pro kit."],
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
    slug="pink-pony-streamathon", featured=False,
    title="Pink Pony Streamathon", client="G2 Esports · Ralph Lauren", via="In-house", year="2021",
    platforms="Twitch, X, Instagram", cat="Charity live event",
    thumb=("i", "pink-pony-team"), quote="552K live viewers for a good cause.",
    summary="The first Pink Pony Streamathon: a three-hour live charity event from Berlin with G2 Esports and Ralph Lauren, supporting young people with cancer at The Royal Marsden.",
    challenge=["A new addition to Ralph Lauren's long-running Pink Pony campaign, so there was no previous event to build on. It needed a live audience big enough to matter "
               "and a tone that respected the cause while still feeling like a G2 stream."],
    role=["I managed the social campaign and the broadcast operations."],
    approach=["Promote it like a G2 event, with players, hosts and music announced in the run-up, then make the stream itself the content, "
              "with donations open throughout the evening."],
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
    role=["Everything: concept, capture, edit, publishing, community and brand partnerships with OMEN by HP, Intel and Snickers. I also competed at events including TwitchCon and EGX."],
    approach=["Make each piece an event in its own right, build a community on Discord, YouTube and X, and grow year on year."],
    idea=["Origin, a Call of Duty montage that was groundbreaking for its time and got the attention of notable creators including KSI."],
    delivered=["Origin and other gaming montages", "Live streaming: 380 streams in 2018", "Community across Discord, YouTube and X", "Brand relationships with OMEN by HP, Intel and Snickers"],
    results=[("61K", "Views, Origin", "6,500 engagements"), ("49K", "Views, Blood // Water", "1,400 likes"), ("25K", "Views, Gears of War 3 Montage #1", "800 likes")],
    results_note="Streaming results for 2018 are below.",
    creator=True,
    skills=["Content creation", "Editing", "Community building", "Live streaming", "Brand partnerships"],
    media={"hero": [("v", "origin", "Origin")],
           "after_idea": [("i", "origin-ksi-comment", "KSI's comment on Origin"), ("i", "montage-fortnite", "Blood // Water, a Fortnite montage: 49K views, 1,400 likes"), ("i", "montage-gow3", "Gears of War 3 Montage #1: 25K views, 800 likes")]},
))
