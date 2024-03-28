# FastAPI application entry point
from fastapi import FastAPI
from .core.config import settings
from .core.events import create_start_app_handler, create_stop_app_handler

app = FastAPI(title=settings.PROJECT_NAME)

@app.get("/")
async def root():
    return {"message": "Hello World"}
from .endpoints.playwright import router as playwright_router
app.include_router(playwright_router, prefix='/playwright', tags=['playwright'])
from .endpoints.metadata import router as metadata_router
app.include_router(metadata_router, prefix='/metadata', tags=['metadata'])
from .endpoints.script import router as script_router
app.include_router(script_router, prefix='/script', tags=['script'])
from .endpoints.act import router as act_router
app.include_router(act_router, prefix='/act', tags=['act'])
from .endpoints.scene import router as scene_router
app.include_router(scene_router, prefix='/scene', tags=['scene'])
from .endpoints.character import router as character_router
app.include_router(character_router, prefix='/character', tags=['character'])
from .endpoints.dialogue import router as dialogue_router
app.include_router(dialogue_router, prefix='/dialogue', tags=['dialogue'])
from .endpoints.action import router as action_router
app.include_router(action_router, prefix='/action', tags=['action'])
from .endpoints.transition import router as transition_router
app.include_router(transition_router, prefix='/transition', tags=['transition'])
from .endpoints.parenthetical import router as parenthetical_router
app.include_router(parenthetical_router, prefix='/parenthetical', tags=['parenthetical'])
from .endpoints.note import router as note_router
app.include_router(note_router, prefix='/note', tags=['note'])
from .endpoints.centered_text import router as centered_text_router
app.include_router(centered_text_router, prefix='/centered_text', tags=['centered_text'])
from .endpoints.page_break import router as page_break_router
app.include_router(page_break_router, prefix='/page_break', tags=['page_break'])
from .endpoints.section_heading import router as section_heading_router
app.include_router(section_heading_router, prefix='/section_heading', tags=['section_heading'])
from .endpoints.title_page import router as title_page_router
app.include_router(title_page_router, prefix='/title_page', tags=['title_page'])
from .endpoints.casting import router as casting_router
app.include_router(casting_router, prefix='/casting', tags=['casting'])
from .endpoints.character_relationship import router as character_relationship_router
app.include_router(character_relationship_router, prefix='/character_relationship', tags=['character_relationship'])
from .endpoints.music_sound import router as music_sound_router
app.include_router(music_sound_router, prefix='/music_sound', tags=['music_sound'])
from .endpoints.props import router as props_router
app.include_router(props_router, prefix='/props', tags=['props'])
from .endpoints.revision_history import router as revision_history_router
app.include_router(revision_history_router, prefix='/revision_history', tags=['revision_history'])
from .endpoints.formatting_rules import router as formatting_rules_router
app.include_router(formatting_rules_router, prefix='/formatting_rules', tags=['formatting_rules'])
from .endpoints.cross_references import router as cross_references_router
app.include_router(cross_references_router, prefix='/cross_references', tags=['cross_references'])
from .endpoints.extended_notes_research import router as extended_notes_research_router
app.include_router(extended_notes_research_router, prefix='/extended_notes_research', tags=['extended_notes_research'])
from .endpoints.scene_location import router as scene_location_router
app.include_router(scene_location_router, prefix='/scene_location', tags=['scene_location'])

# Add additional routes here
