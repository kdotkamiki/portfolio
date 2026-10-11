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
HOME_INTRO = (
    "Strategy that finds the moment. Ideas that own it. Content that earns the scroll. "
    "I lead social-first creative for culture, esports and B2B tech brands: "
    "organic at the core, paid to scale, judged on results."
)

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
    "The through-line is the same in B2B and B2C: find the cultural moment a brand has a right to own, "
    "build one idea strong enough to travel across platforms and markets, make every version feel native "
    "to where it lands, then measure honestly and make the next one better.",
]

STATS = [  # (number, suffix, label) – all verified in SOURCES.md
    (15, "+", "Years in social, content and community"),
    (1000, "+", "Videos delivered between 2020 and 2026"),
    (100, "K", "Scaled a newly launched YouTube channel to 100K subscribers in year one, earning the Silver Creator Award."),
    (2021, "", "Esports Creative Piece of the Year, G2 Esports × adidas"),
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
    slug="vct-emea-2024-season-teasers", featured=True,
    title="VCT EMEA 2024: Season Teasers", client="Riot Games", via="At Edelman", year="2024–25",
    platforms="YouTube, X, Instagram, TikTok", cat="Tentpole campaign films",
    thumb=("v", "vct24-kickoff-teaser"), quote="New meta. New faces. New ambitions.",
    summary="The films that opened, restarted and closed VALORANT's EMEA league in its biggest year so far, each built around what was new at that point in the season.",
    challenge=["2024 brought a new Kickoff tournament, a new team promoted through Ascension, and a season split into stages. "
               "Each stage needed its own reason to tune in, without repeating the same hype formula the audience had already seen."],
    role=[ED,
          "On the season teasers I led creative development and campaign planning: writing and shaping the creative briefs, "
          "working with video studio partners from concept to final cut, aligning Riot's product, brand and game teams, "
          "and building the cross-platform rollout. On the 2025 Kickoff teaser, my role was creative input and social campaign planning."],
    approach=["A tentpole system that makes every chapter of the season feel like an event:",
              ("steps", [("Find the story of the moment", "Kickoff is about change, Stage 2 about a new look and new stakes, the Grand Finals about legacy."),
                         ("Give each chapter a distinct creative world", "New visual language and tone each time, so the audience never feels they've seen it before."),
                         ("Build on the 2024 brand", "Use the league's new colours and imagery as the connective tissue across every film."),
                         ("Cut natively for every platform", "Bespoke edits for YouTube, X, Instagram and TikTok rather than one asset shared everywhere."),
                         ("Launch, read, iterate", "Track reach, engagement and sentiment per teaser and carry the learnings into the next chapter.")])],
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
    slug="valorant-masters-madrid", featured=True,
    title="VALORANT Masters Madrid", client="Riot Games", via="At Edelman", year="2024",
    platforms="YouTube, X, Instagram, TikTok", cat="International event hype",
    thumb=("v", "masters-madrid-hello"), quote="Hello, Madrid.",
    summary="Creative direction for the hype campaign around VALORANT Masters Madrid 2024, the first international event of the season, as it arrived in a new host city.",
    challenge=["International events compete with every other moment in the esports calendar. The job was to generate hype for Madrid: "
               "make the event feel unmissable to existing fans and give the host city a role in the story."],
    role=[ED,
          "On Masters Madrid my role was creative direction: setting the creative vision, briefing and guiding the production team, "
          "reviewing cuts against the brief and making sure the finished film was built to perform on social."],
    approach=["Hype built on a sense of place:",
              ("steps", [("Start from the city", "Make Madrid itself a character, not just a backdrop for logos and dates."),
                         ("Bridge the season", "Connect the EMEA league to the international stage so fans feel the jump in stakes."),
                         ("Build to the reveal", "Pace the film towards the Masters Madrid moment and the event branding."),
                         ("Distribute natively", "Cut and sequence the film for each platform in the run-up to the event.")])],
    idea=["Hello, Madrid: a journey into the host city that lands on the Masters Madrid reveal, announcing that VALORANT's international stage has arrived."],
    delivered=["Creative direction on the Hello Madrid hype film", "Social rollout in the run-up to the event"],
    results=[],
    results_note="Performance data for this film wasn't part of the material supplied, so none is shown here.",
    skills=["Creative direction", "Event marketing", "Brand storytelling", "Video production"],
    media={"hero": [("v", "masters-madrid-hello", "Hello Madrid: VALORANT Masters Madrid 2024")]},
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
    slug="meet-the-player", featured=True,
    title="Meet the Player", client="Riot Games", via="At Edelman", year="2024",
    platforms="YouTube, X, Instagram", cat="Player documentary series",
    thumb=("v", "love-what-you-do-mimi"), quote="Players, at home.",
    summary="A series of mini-documentaries about players' lives in and outside VALORANT, starting with G2's Mimi in her hometown in Denmark.",
    challenge=["Fans know players through their gameplay, not as people. Reach-led formats grow numbers but rarely build lasting fandom for individual players."],
    role=[ED,
          "On this series I helped select the players worth featuring, shaped the editorial angle for each film, supported the on-location production "
          "and set the measurement framework, putting sentiment and engagement ahead of reach."],
    approach=["Depth over reach, by design:",
              ("steps", [("Pick the right players", "Identify the people in the league with a story worth telling, not just the biggest names."),
                         ("Go to the source", "Film in their hometowns, so the story is told through the places that shaped them."),
                         ("Tell the whole career", "The highs and the lows, inside the game and outside it."),
                         ("Measure what the format is for", "Sentiment and engagement as the KPIs, because documentary content builds affinity rather than raw reach.")])],
    idea=["Meet the Player: the ups and downs of a career, inside the game and outside it, told at home. For Mimi, that meant filming in her hometown in Denmark."],
    delivered=["Four player feature films", "On-location shoot in Denmark for the Mimi episode", "Social cutdowns and distribution"],
    results=[("99%+", "Positive sentiment", ""), ("8,000+", "Engagements across the four films", "")],
    results_note="",
    skills=["Documentary storytelling", "Talent development", "Sentiment-led measurement", "Video production"],
    media={"hero": [("v", "love-what-you-do-mimi", "Meet the Player: G2 Mimi")]},
))

P.append(dict(
    slug="join-us-vct-emea-2023", featured=True,
    title="Join Us: VCT EMEA 2023", client="Riot Games", via="In-house", year="2023",
    platforms="YouTube, X, Instagram, TikTok", cat="League launch",
    thumb=("v", "join-us"), quote="A new league, introduced by its players.",
    summary="The launch films for the 2023 season of VCT EMEA, the first year of VALORANT's partnership league: Join Us, and the opening teaser.",
    challenge=["2023 was a new structure for VALORANT esports in EMEA, with ten partner teams and a new studio in Berlin. "
               "Fans needed a reason to commit to a league they hadn't seen yet."],
    role=[RG,
          "For the launch, I set the social and creative strategy, worked with the creative and production teams on the concept and shoot, "
          "planned the content calendar and rollout across channels, and owned performance tracking after launch."],
    approach=["A people-first launch campaign:",
              ("steps", [("Lead with the players", "Personalities sell a new league faster than logos and formats do."),
                         ("Make it local", "Put the players in ordinary places around Berlin, the league's new home."),
                         ("Sequence the launch", "The Join Us film to invite fans in, then a cinematic opening teaser on the eve of the season."),
                         ("Extend the shoot", "Photography from the same shoot to feed launch-week posts and always-on content.")])],
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
    role=[RG,
          "On Unlocked, I owned the series as part of the 2023 launch campaign: defining the format and editorial angle, coordinating with the ten partner teams, "
          "working with production on the shoots and edits, and planning the YouTube release schedule and social cut-downs."],
    approach=["Hype the league by growing every team's fandom:",
              ("steps", [("One episode per partner team", "Every organisation gets the same platform, so no fanbase is left out."),
                         ("Go to their roots", "Film in each team's hometown and headquarters."),
                         ("Let the players talk", "Their motivations, their goals and what they're excited about this season."),
                         ("Release into Kickoff", "Schedule episodes in the run-up to the league launch and cut them down for social.")])],
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
    slug="frenzy-fire", featured=True,
    title="Frenzy Fire", client="Riot Games", via="In-house, then at Edelman", year="2023–24",
    platforms="YouTube, X, Instagram, TikTok", cat="Quiz series",
    thumb=("i", "frenzy-fire-ninja-defuse"), quote="How well do pros know their own game?",
    summary="A quick-fire quiz series that tests VCT EMEA pros on their own game and league, and became one of the league's most popular formats.",
    challenge=["The league needed always-on content between broadcasts that showed players' personalities, was efficient to produce, and worked in clips across platforms."],
    role=["Frenzy Fire was part of the VCT EMEA content slate I led at Riot Games in 2023: I owned the format's place in the content strategy, "
          "planned the question sets and player line-ups with production, and managed publishing and cut-downs across platforms.",
          "At Edelman in 2024, I carried the series forward, evolving the format and tracking its year-on-year growth."],
    approach=["An always-on franchise engineered for repeatability and reach:",
              ("steps", [("Keep the format simple", "Quick-fire questions, a scoreboard and players who really want to win."),
                         ("Make it work with any player", "The same format scales across the whole league, every week."),
                         ("Build for clipping", "Every round is a standalone moment for Shorts, Reels, TikTok and X."),
                         ("Evolve in season two", "New mechanics in 2024, with players guessing which pro said a given quote.")])],
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
    role=[RG,
          "On Lock Your Tickets I owned the social campaign: the creative brief for the trailer, the organic rollout, and the paid set-up with our media partners, "
          "with UTM tracking on every link so ticket clicks and purchases could be attributed back to the creative."],
    approach=["A conversion-led, full-funnel ticketing campaign:",
              ("steps", [("Lead with hype", "A trailer that makes the live room feel like the place the season happens."),
                         ("Put paid behind it", "Paid social to reach in-market fans beyond the organic audience."),
                         ("Track every click", "UTMs on all links, so performance is read against ticket demand, not just views."),
                         ("Optimise on conversion", "Shift spend and messaging towards what was actually selling tickets.")])],
    idea=["Lock Your Tickets: a fast, red-drenched trailer that makes the live room feel like the place the season happens."],
    delivered=["Ticketing trailer", "Paid social campaign with UTM tracking", "Organic launch posts"],
    results=[("~600K", "Views", ""), ("~10%", "Conversion rate on UTM clicks", ""), ("527.2K", "Views on the launch post on X", "")],
    results_note="",
    skills=["Paid social", "Performance tracking", "Conversion-led creative", "Event marketing"],
    media={"hero": [("v", "lock-your-tickets", "Lock Your Tickets trailer"), ("i", "lock-tickets-tweet", "Launch post on X: Watch your favourite VCT EMEA team live at our Coliseum in Berlin Messe")]},
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
    slug="gekko-truck-and-fan-wall", featured=True,
    title="Gekko's Bubble Tea Truck & the Fan Wall", client="Riot Games", via="In-house", year="2023",
    platforms="IRL, X, Instagram", cat="Experiential",
    thumb=("i", "gekko-5"), hero=("i", "gekko-1"), quote="Free bubble tea. Fans asked for it back.",
    summary="Two in-person moments for VALORANT fans in Berlin: Gekko's bubble tea truck, part of a wider out-of-home campaign, and a signed wall that made the fans part of the league's history.",
    challenge=["The studio in Berlin gave the league a physical home. The opportunity was to give fans things to do there, and around the city, that they'd share and remember."],
    role=[RG,
          "The Gekko bubble tea truck was part of a larger out-of-home campaign, and I managed the social side of it end to end: "
          "the content plan, capture on site, community engagement and reporting on sentiment and reach. "
          "The fan wall was my idea, planned from the start as both a social moment and a piece of VCT EMEA history."],
    approach=["Experiential, designed to be shared:",
              ("steps", [("IRL first", "Build experiences people genuinely want to be part of."),
                         ("Social by design", "Make every activation photographable and give fans a reason to post it."),
                         ("Extend the reach", "Turn the truck's run around Berlin and its time in the studio into social content for fans who weren't there."),
                         ("Leave something behind", "A fan wall that lives on after the event as part of the league's story.")])],
    idea=[("h", "Gekko's bubble tea truck"),
          "A VALORANT-branded bubble tea truck themed on the agent Gekko, for bubble tea fans and VALORANT fans alike, as part of a wider 2023 out-of-home campaign. "
          "It was parked near Alexanderplatz in Berlin for three weekends only, then came into the studio, where visitors used the tokens they got on entry to redeem a free drink.",
          ("h", "The fan wall"),
          "A VCT EMEA-branded wall at the Coliseum where fans could sign their names and leave their mark on the league's history."],
    delivered=["Social campaign for the Gekko truck, end to end", "Fan wall concept and activation", "Social content from both"],
    results=[("2,000+", "Free bubble teas served", "")],
    results_note="The truck was measured on sentiment and reach. It was one of the most popular activations of the year, and fans asked for it to come back.",
    skills=["Experiential", "Out-of-home", "Fan engagement", "Social-first activation", "Community"],
    media={"hero": [("i", "gekko-5", "Gekko's bubble tea truck in Berlin")],
           "after_approach": [("i", "gekko-6", "Serving bubble tea from the truck"), ("i", "gekko-3", "VALORANT-themed bubble tea")],
           "after_idea": [("i", "gekko-9", "The truck in the VCT EMEA studio"), ("i", "gekko-8", "Gekko artwork on the truck"), ("i", "gekko-tweet", "VALORANT Esports EMEA post on X about the Gekko truck")],
           "after_delivered": [("i", "fan-wall", "The signed VCT EMEA fan wall")],
           "after_results": [("i", "fan-wall-tweet", "VALORANT Esports EMEA post on X about the fan wall")]},
))

P.append(dict(
    slug="vct-emea-2023-content-slate", featured=True,
    title="The 2023 Content Slate", client="Riot Games", via="In-house", year="2023",
    platforms="YouTube, X, Instagram, TikTok", cat="Always-on content",
    thumb=("grid", ["showstopper", "do-it-yourself", "first-champs", "ascension-promo"]), quote="A season's worth of reasons to watch.",
    summary="The always-on series, promos and programmes that carried VCT EMEA through its first partnership season, alongside the tentpole campaigns.",
    challenge=["A league season runs for months. Between the big moments, the channels needed a steady rhythm of content that grew fandom for teams, players and the competition itself."],
    role=[RG,
          "Across the slate I set the content strategy and led delivery: briefing and managing agencies and production vendors, building content calendars, "
          "running the influencer programme with creators on the ground in the studio, and reporting performance to optimise the mix. "
          "On the Game Changers promo, my role was creative input and social campaign planning."],
    approach=["A content ecosystem with a format for every kind of fan:",
              ("steps", [("Segment the audience", "Competitive fans, long-time fans, new fans and creators' communities all want different things."),
                         ("Assign a format to each", "Rivalries for the competitive, nostalgia for long-time fans, personality for new ones, creators to bring the league to their own communities."),
                         ("Set a rhythm", "Weekly series between the tentpoles so the channels never go quiet."),
                         ("Optimise the mix", "Track each format and put more behind what's working.")])],
    idea=None,
    slate=[
        ("Showstopper", "showstopper", "v", "Two-to-three-minute films about the rivalries between regions, countries and teams, promoting each week's broadcast.", "260K views · ~7K engagements"),
        ("Ascension promo", "ascension-promo", "v", "A highly abstract promo for Ascension, where tier 2 teams compete for a place in the league. I co-created it with a Madrid-based studio.", "50K reach · 2K engagements"),
        ("First Champs", "first-champs", "v", "Reuniting the first-ever VCT champions, from EMEA, in a piece of league history fans could rally behind.", "40K reach · 2K engagements"),
        ("Do It Yourself", "do-it-yourself", "v", "A three-episode series.", "100K views · ~8K engagements"),
        ("Talent announcement", "talent-announcement", "v", "An unconventional talent announcement: a video instead of a static graphic, crossing over with the League of Legends LEC studio and talent.", "~10K reach · ~700 engagements, above average for this kind of announcement"),
        ("Admission forms", "admission-form", "i", "Players filled in admission forms with personal facts and quirky drawings, inspired by how Formula 1 and other top sports present athletes.", "~100K reach · ~6K engagements"),
        ("Influencer watch parties", "influencer-watch-parties", "i", "Weekly watch parties hosted by creators, plus on-the-ground content with them in the studio.", "1M+ reach across hundreds of influencers"),
        ("Game Changers EMEA promo", "game-changers-promo", "v", "Promo film for VCT Game Changers EMEA 2023. My role: creative input and social campaign planning.", ""),
    ],
    delivered=["Showstopper rivalry series", "Ascension promo", "First Champs", "Do It Yourself series", "Talent announcement film",
               "Player admission forms", "Influencer watch party programme", "Game Changers EMEA promo"],
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


# One-line overview shown under the title and labels on work cards. Each is a
# condensed version of the project's own summary above, so no new claims.
LINES = {
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
    "vct-emea-2023-content-slate": "The always-on series that carried VCT EMEA through its first partnership season.",
    "g2-esports-x-adidas": "The social launch of adidas as G2 Esports' official apparel partner.",
    "pink-pony-streamathon": "A three-hour live charity stream from Berlin supporting young people with cancer.",
    "origin-and-the-creator-years": "Twelve years of making my own content, from gaming montages to full-time streaming.",
}
for _p in P:
    _p["line"] = LINES[_p["slug"]]
