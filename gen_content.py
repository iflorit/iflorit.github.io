#!/usr/bin/env python3
from build_articles import build, faq_schema, howto_schema, render_faq_html, cta

SLUG_TITLES = [
    ("loud-alarm-before-zoom-teams-meetings-iphone", "How to Get a Loud Alarm Before Zoom or Teams Meetings on iPhone"),
    ("iphone-calendar-alerts-too-quiet-fixes", "iPhone Calendar Alerts Too Quiet? Fixes for Meeting Reminders"),
    ("never-miss-meeting-live-activities-dynamic-island", "Never Miss a Meeting: Live Activities and Dynamic Island Countdowns"),
]

# ---------------------------------------------------------------------------
# Article 1
# ---------------------------------------------------------------------------
a1_slug = SLUG_TITLES[0][0]
a1_qa = [
    ("Will a Calendar notification wake me up if my iPhone is on silent?",
     "No. Standard Calendar and Reminders notifications respect Silent mode and most Focus modes by default — they show up on screen but make no sound and don't vibrate unless you've changed your settings. If you need an audible alert on silent, you need something that uses the Clock app's alarm system, which is built to bypass the silent switch."),
    ("Does Do Not Disturb block meeting alerts too?",
     "By default, yes. Do Not Disturb silences calls, texts, and notifications, including calendar alerts, unless you've added specific contacts or apps to an allow list. A few apps request permission to break through Focus for Time Sensitive notifications, but that still isn't the same as a real alarm."),
    ("What's the actual difference between a notification and an alarm on iPhone?",
     "A notification is a banner and optional sound managed by Notification Center; it obeys Silent mode and Focus. An alarm, set through the Clock app or an app built on Apple's AlarmKit, rings at full ringer volume and bypasses both the silent switch and Do Not Disturb — the same behavior as your morning wake-up alarm."),
]
a1_body = f"""
<p>If a Zoom or Teams call has ever started without you because your phone was face-down and silenced, the fix isn't a louder notification — it's a real alarm.</p>

<h2>Why calendar notifications don't wake you up</h2>
<p>iOS treats calendar reminders as regular notifications. Regular notifications check the state of the silent switch and your active Focus mode before making a sound. If either one says "quiet," the notification stays quiet — you'll see it when you pick up your phone, which is often too late.</p>
<p>Alarms work differently. They're a separate subsystem tied to the Clock app, and they're allowed to ring at full volume no matter what the silent switch or Focus is set to. That's the mechanism you actually want for a meeting you can't afford to miss.</p>

<h2>Option 1: Set a manual alarm for each meeting</h2>
<p>The most reliable native option is also the most tedious: open the Clock app, add an alarm for the exact time your call starts, and label it. It will ring through silent and Do Not Disturb every time, because that's what alarms are designed to do.</p>
<ul>
<li>Open <strong>Clock → Alarm → +</strong>.</li>
<li>Set the time your meeting starts (or a few minutes before, to give yourself a buffer).</li>
<li>Give it a label so you know which meeting it's for.</li>
</ul>
<p>The catch: you have to do this manually for every single meeting, remember to delete it afterward, and re-create it if the meeting moves. For a calendar with more than a couple of calls a day, that adds up fast.</p>

<h2>Option 2: Turn up notification sounds and check your Focus allow list</h2>
<p>If a full alarm feels like overkill, you can at least make sure your calendar app is allowed to make noise:</p>
<ul>
<li>Go to <strong>Settings → Focus</strong> and check whether Do Not Disturb or Work is active during your meeting hours — if so, add your calendar app to the allowed apps/people list, or allow Time Sensitive notifications.</li>
<li>In <strong>Settings → Sounds & Haptics</strong>, confirm your ringer volume isn't turned all the way down, since notification sounds share that volume.</li>
<li>Check that the silent switch (or Action Button on iPhone 15 and later) isn't set to silent during meeting hours.</li>
</ul>
<p>This helps, but it's still a notification, not an alarm — it can be dismissed by mistake or missed under a stack of other banners, and it still won't sound if the phone is physically in silent mode.</p>

<h2>Option 3: Use an app built on AlarmKit for per-meeting alarms</h2>
<p>Apple's AlarmKit framework, introduced for third-party apps, lets an app schedule real alarms — the kind that ring through silent and Focus — tied to specific events, without you setting each one by hand in the Clock app.</p>
<p><strong>Call to Meet</strong> reads the calendars you already use and sets one of these real alarms automatically before each meeting, up to 8 hours ahead. It also shows a live countdown on your Lock Screen and in the Dynamic Island so you can see at a glance how much time is left, and a one-tap Join button for Zoom, Google Meet, and Microsoft Teams once the alarm fires. It runs on iOS 26 or later, since that's the OS version AlarmKit ships in.</p>
{cta(a1_slug)}
{render_faq_html(a1_qa)}
"""

# ---------------------------------------------------------------------------
# Article 2
# ---------------------------------------------------------------------------
a2_slug = SLUG_TITLES[1][0]
a2_steps = [
    {"name": "Check your ringer volume", "text": "Go to Settings > Sounds & Haptics and make sure the ringer and alert volume isn't set low — notification sounds, including calendar alerts, use this same volume."},
    {"name": "Review your Focus modes", "text": "Open Settings > Focus and check each Focus (Do Not Disturb, Work, Sleep) that might be active during your meetings. Add your calendar app to the allowed list or enable Time Sensitive notifications so alerts can get through."},
    {"name": "Pick a distinct alert sound", "text": "In the Calendar app, go to a specific event or your default alert settings and choose a sound that's easy to distinguish from other notifications, so you notice it even in a noisy environment."},
    {"name": "Add a second, earlier alert", "text": "Most calendar apps let you stack multiple alerts per event (for example, 15 minutes and 1 minute before). A second alert closer to start time reduces the chance you miss the first one."},
    {"name": "Switch to a real alarm for meetings that matter", "text": "For calls you truly cannot miss, use the Clock app's alarm — or an app that sets one automatically — since alarms bypass Silent mode and Focus in a way regular notifications don't."},
]
a2_qa = [
    ("Why does my iPhone calendar alert make no sound sometimes?",
     "The most common causes are the silent switch being on, an active Focus mode blocking the Calendar app, or the ringer/alert volume being turned down in Settings > Sounds & Haptics. Calendar alerts are standard notifications, so they follow whatever your device's current sound and Focus settings say."),
    ("Can I make one calendar alert louder than the others?",
     "Not louder in terms of volume, but you can assign a more distinct alert sound per event or calendar in the Calendar app, which makes it easier to notice among other notifications. True volume control only exists at the system level for alarms, not individual notifications."),
    ("Is there a way to get an alert that ignores Do Not Disturb entirely?",
     "Yes — an alarm. Alarms set through the Clock app, or through a third-party app using Apple's AlarmKit, ring at full volume regardless of Do Not Disturb, Focus, or the silent switch. That's the only mechanism on iOS designed to override those settings."),
]
a2_body = f"""
<p>A quiet meeting alert is worse than no alert at all — it gives you a false sense that you'll notice in time. Here's what's actually adjustable on iPhone, and where those adjustments stop working.</p>

<h2>Start with the basics: volume, Focus, and the silent switch</h2>
<p>Before assuming anything is broken, check the three settings that most commonly mute calendar alerts:</p>
<ol>
<li><strong>Ringer and alert volume</strong> — in Settings > Sounds & Haptics, drag the slider up and test with the phone unlocked.</li>
<li><strong>Active Focus mode</strong> — Work, Sleep, and Do Not Disturb can each have a different allow list. Check whichever one is active during your meeting hours.</li>
<li><strong>The silent switch or Action Button</strong> — if it's flipped to silent, standard notifications, including calendar alerts, won't make a sound, even if the volume is turned up.</li>
</ol>

<h2>Step-by-step: tuning your calendar alerts</h2>
<ol>
<li>Open <strong>Settings → Sounds & Haptics</strong> and confirm the ringer/alert volume is audible.</li>
<li>Open <strong>Settings → Focus</strong>, tap into each Focus you use, and add Calendar (and any meeting apps) to the allowed apps, or enable Time Sensitive notifications.</li>
<li>In the <strong>Calendar app</strong>, open an event's alert settings and pick a distinct sound, or set your default alert sound under calendar preferences.</li>
<li>Add a <strong>second alert</strong> closer to the meeting's start time so you get two chances to notice.</li>
<li>For meetings you genuinely can't miss, set a <strong>real alarm</strong> instead of relying on notifications.</li>
</ol>

<h2>Where notification tuning hits a wall</h2>
<p>Even with every setting maximized, a calendar alert is still a notification — it respects the silent switch by design. If your phone is physically silenced when the alert fires, you won't hear it, no matter how loud your alert sound is configured to be. Apple builds it this way on purpose: silent mode is supposed to mean silent.</p>
<p>The same applies to a locked screen sitting face-down on a desk: a notification banner can render, chime, and disappear again while your attention is elsewhere, and there's no mechanism that forces you to notice it. Multiple stacked notifications from other apps can also push a calendar alert out of view before you ever see it.</p>

<h2>When it's worth switching to a real alarm</h2>
<p>Not every meeting needs this level of insurance — a standup you can join a minute late is fine with a regular notification. But for calls where being late has a real cost (an interview, a client demo, a doctor's appointment reschedule), the reliability gap between "notification" and "alarm" stops being theoretical.</p>
<p>That's exactly the gap AlarmKit-based alarms are built to close. <strong>Call to Meet</strong> uses it to set a real, per-meeting alarm — reading your existing calendars automatically, ringing through silent and Focus up to 8 hours ahead of each meeting, with a live countdown on your Lock Screen and Dynamic Island so you always know what's next and when. You still get the same calendar you already use; the alarm layer is additive, not a replacement for it.</p>
{cta(a2_slug)}
{render_faq_html(a2_qa)}
"""

# ---------------------------------------------------------------------------
# Article 3
# ---------------------------------------------------------------------------
a3_slug = SLUG_TITLES[2][0]
a3_qa = [
    ("What is a Live Activity on iPhone?",
     "A Live Activity is a small, glanceable card that appears on your Lock Screen and updates in real time, without you unlocking the phone or opening the app. Apple introduced them for things like sports scores and delivery tracking; apps like Call to Meet use them to show a live countdown to your next meeting."),
    ("What's the difference between the Dynamic Island and the Lock Screen for this?",
     "They're two surfaces for the same Live Activity. The Lock Screen version shows when your phone is locked. The Dynamic Island version shows at the top of the screen while you're actively using the phone — in Messages, Safari, or any other app — so the countdown follows you without switching apps."),
    ("Do Live Activities and Dynamic Island countdowns work without an alarm?",
     "Yes, they're separate features. A Live Activity is a visual, glanceable countdown; an alarm is an audible alert. Call to Meet uses both together — the countdown so you always see what's next, and a real alarm (via AlarmKit) so you don't have to be looking at the screen to be alerted."),
]
a3_body = f"""
<p>Even with alerts turned on, it's easy to lose track of exactly how much time is left before a call. Live Activities and the Dynamic Island solve a different problem than alarms: they keep the countdown visible, continuously, without you having to open an app.</p>

<h2>What a Live Activity actually shows you</h2>
<p>A Live Activity is a compact, auto-updating card that Apple's system displays on your Lock Screen. Instead of a static notification you dismiss once, it stays there and refreshes itself — showing a countdown, a progress bar, or both — for as long as the activity is running. You don't need to unlock your phone to see how much time is left before your next meeting.</p>

<h2>The Dynamic Island: the same countdown, while you're using your phone</h2>
<p>On iPhones with a Dynamic Island, the same Live Activity also surfaces at the top of the screen whenever your phone is unlocked and you're in another app — checking Slack, replying to a text, browsing. Tap it and it expands to show more detail; tap again and you can jump straight into the meeting. It's the closest thing iOS has to an always-on status bar for "what's next."</p>

<h2>Why this matters more than a single notification</h2>
<ul>
<li><strong>Notifications disappear.</strong> Once you swipe one away, the information is gone. A Live Activity stays put and keeps updating.</li>
<li><strong>You don't have to remember to check the calendar.</strong> The countdown is already on the screen you're looking at.</li>
<li><strong>It scales down anxiety about "did I miss it."</strong> A visible, ticking countdown removes the need to keep unlocking your phone to check the time.</li>
</ul>

<h2>How Call to Meet uses both</h2>
<p>Call to Meet reads your existing calendars and turns each upcoming meeting into a live countdown — on the Lock Screen as a Live Activity, and in the Dynamic Island while you're using your phone. When it's time to join, tap through to Zoom, Google Meet, or Microsoft Teams in one step, or dial in by phone if the meeting has a number. Paired with a real AlarmKit alarm that rings even on silent, you get both the visual countdown and the audible alert that make it very hard to miss the meeting — without opening the calendar app to check.</p>
{cta(a3_slug)}
{render_faq_html(a3_qa)}
"""

ARTICLES = [
    dict(
        slug=a1_slug,
        title="How to Get a Loud Alarm Before Zoom or Teams Meetings on iPhone (Even on Silent) | Call to Meet",
        description="Calendar notifications stay quiet on silent iPhone. Here's how alarms work differently, native ways to fix it, and when an app-set AlarmKit alarm is worth it.",
        kicker="iPhone · Meeting alerts",
        h1="How to get a loud alarm before Zoom or Teams meetings on iPhone (even on silent)",
        dek="Calendar notifications go quiet the moment your iPhone is silenced. Alarms don't. Here's the difference, and three ways to fix it.",
        body_html=a1_body,
        schemas=[faq_schema(f"https://iflorit.github.io/{a1_slug}.html", a1_qa)],
    ),
    dict(
        slug=a2_slug,
        title="iPhone Calendar Alerts Too Quiet? Fixes for Meeting Reminders | Call to Meet",
        description="Step-by-step fixes for quiet iPhone calendar alerts: volume, Focus allow lists, alert sounds, and where notification settings stop working entirely.",
        kicker="iPhone · Troubleshooting",
        h1="iPhone calendar alerts are too quiet: fixes for meeting reminders",
        dek="Before you assume something's broken, check these five settings — then learn where calendar notifications hit a hard limit that only a real alarm can cross.",
        body_html=a2_body,
        schemas=[
            howto_schema(
                "Fix quiet calendar alerts on iPhone",
                "Steps to make iPhone calendar meeting alerts audible again.",
                a2_steps,
            ),
            faq_schema(f"https://iflorit.github.io/{a2_slug}.html", a2_qa),
        ],
    ),
    dict(
        slug=a3_slug,
        title="Never Miss a Meeting on iPhone: Live Activities & Dynamic Island Countdowns | Call to Meet",
        description="How Live Activities and the Dynamic Island keep a live meeting countdown on your iPhone's Lock Screen and status bar, without opening an app.",
        kicker="iPhone · Live Activities",
        h1="Never miss a meeting on iPhone: Live Activities and Dynamic Island countdowns",
        dek="A notification disappears the moment you dismiss it. A Live Activity stays on screen and keeps counting down. Here's how that changes meeting reminders.",
        body_html=a3_body,
        schemas=[faq_schema(f"https://iflorit.github.io/{a3_slug}.html", a3_qa)],
    ),
]

if __name__ == "__main__":
    for art in ARTICLES:
        slug = build(art, SLUG_TITLES)
        print("built", slug)
