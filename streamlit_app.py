import streamlit as st
import streamlit.components.v1 as components

components.html(
    """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Soul Guard</title>
</head>
<body>
  <div class="LandingPage" style="width: 375px; height: 1271px; background: white; display: flex; flex-direction: column; justify-content: flex-start; align-items: flex-start;">
    <div class="HeroImage" style="width: 100%; height: 207px; padding: 160px 24px; background: #E8B931; display: flex; flex-direction: column; justify-content: center; align-items: center; gap: 32px;">
      <div class="TextContentTitle" style="display: flex; flex-direction: column; justify-content: flex-start; align-items: center; gap: 8px;">
        <div class="Title" style="text-align: center; color: #02542D; font-size: 48px; font-family: Inter; font-weight: 700; line-height: 57.6px;">Soul Guard</div>
        <div class="Subtitle" style="text-align: center; color: #02542D; font-size: 32px; font-family: Inter; font-weight: 400; line-height: 38.4px;">Signals of Support</div>
      </div>
      <div class="ButtonGroup" style="display: flex; justify-content: center; align-items: center; gap: 16px;">
        <div class="Button" style="padding: 12px; background: #30B0C7; border-radius: 8px; border: 1px solid #767676; display: flex; justify-content: center; align-items: center;">
          <div class="ButtonText" style="color: #1E1E1E; font-size: 16px; font-family: Inter; font-weight: 400;">For You</div>
        </div>
        <div class="Button" style="padding: 12px; background: #30B0C7; border-radius: 8px; border: 1px solid #2C2C2C; display: flex; justify-content: center; align-items: center;">
          <div class="ButtonText" style="color: #F5F5F5; font-size: 16px; font-family: Inter; font-weight: 400;">For Whom You Care</div>
        </div>
      </div>
    </div>
    <div class="PanelImageContentReverse" style="width: 100%; height: 289px; padding: 24px; opacity: 0.80; background: linear-gradient(0deg, #E3E3E3 0%, #E3E3E3 100%); background-image: url('https://via.placeholder.com/375x289'); display: flex; flex-direction: column; gap: 24px;">
      <div class="TextContentFlow" style="display: flex; flex-direction: column; gap: 24px;">
        <div class="Text" style="color: #007AFF; font-size: 16px; font-family: Inter; font-weight: 400; line-height: 22.4px;">Words, especially on social media, can speak volumes. With expert guidance, we usher the right path to support.</div>
      </div>
    </div>
    <div class="PanelImageDouble" style="width: 100%; height: 292px; padding: 24px; opacity: 0.80; background: linear-gradient(0deg, #E3E3E3 0%, #E3E3E3 100%); background-image: url('https://via.placeholder.com/375x292'); display: flex;"></div>
    <div class="PanelImageDouble" style="width: 100%; height: 295px; padding: 24px; opacity: 0.80; background: linear-gradient(0deg, #E3E3E3 0%, #E3E3E3 100%); background-image: url('https://via.placeholder.com/375x295'); display: flex;"></div>
    <div class="Footer" style="width: 100%; height: 185px; padding: 32px; background: #E8B931; border-top: 1px solid #02542D; display: flex; flex-direction: column; gap: 64px;">
      <div class="Links" style="display: flex; flex-direction: column; gap: 24px;">
        <div class="TextLinkList" style="display: flex; flex-direction: column; gap: 8px;">
          <div class="Title" style="font-size: 16px; font-family: Inter; font-weight: 700; color: #02542D;">Resources</div>
          <div class="TextLinkListItem" style="color: #02542D; font-size: 16px;">Blog</div>
          <div class="TextLinkListItem" style="color: #02542D; font-size: 16px;">Best practices</div>
          <div class="TextLinkListItem" style="color: #02542D; font-size: 16px;">Support Groups</div>
          <div class="TextLinkListItem" style="color: #02542D; font-size: 16px;">Apps we Like</div>
        </div>
      </div>
    </div>
  </div>
</body>
</html>
    """,
    height=600,
)