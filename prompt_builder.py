def build_prompt(initial_prompt: str, answers: dict) -> str:
    """
    Assembles the final structured prompt using answers provided by the user.
    """
    # 1. Determine Role/Persona
    role_selected = answers.get("role", "")
    custom_role = answers.get("custom_role", "").strip()
    
    role = ""
    if role_selected == "Custom (Specify below)" and custom_role:
        role = custom_role
    elif role_selected and role_selected != "Default / General Assistant" and role_selected != "Custom (Specify below)":
        role = role_selected

    # Start compiling sections
    sections = []
    
    # Role Section
    if role:
        sections.append(f"## Role / Persona\nAct as: {role}")
    
    # Task / Core Objective
    sections.append(f"## Core Task\n{initial_prompt.strip()}")
    
    # Context & Details Section
    context_details = []
    
    audience = answers.get("audience", "").strip()
    if audience:
        context_details.append(f"- **Target Audience**: {audience}")
        
    tone = answers.get("tone", "").strip()
    if tone:
        context_details.append(f"- **Tone / Style**: {tone}")
        
    length = answers.get("length", "").strip()
    if length:
        context_details.append(f"- **Length Constraints**: {length}")
        
    language = answers.get("language", "").strip()
    if language:
        context_details.append(f"- **Language / Stack / Framework**: {language}")
        
    error_handling = answers.get("error_handling", "").strip()
    if error_handling:
        context_details.append(f"- **Code Style & Quality**: {error_handling}")
        
    data_input = answers.get("data_input", "").strip()
    if data_input:
        context_details.append(f"- **Input Data Details**: {data_input}")
        
    if context_details:
        sections.append("## Context & Guidelines\n" + "\n".join(context_details))
    
    # Format Section
    output_format = answers.get("format", "").strip()
    if output_format:
        sections.append(f"## Expected Output Format\nProvide the response as: {output_format}")
        
    # Constraints Section
    constraints = answers.get("constraints", "").strip()
    if constraints:
        # If the user didn't write it as bullet points, let's keep it clean
        sections.append(f"## Strict Constraints & Exclusions\n{constraints}")
        
    # Examples Section (Few-Shot)
    examples = answers.get("examples", "").strip()
    if examples:
        sections.append(f"## Examples / Few-Shot Reference\nUse the following examples to guide your response pattern:\n\n{examples}")

    # Compile the final system prompt block
    prompt_intro = "Please execute the following task with high precision. Adhere to the specified role, guidelines, and constraints below."
    
    full_prompt = f"{prompt_intro}\n\n" + "\n\n".join(sections)
    return full_prompt
