# Unified YAML Frontmatter Standard for LifeOS v2.0

## Overview
This document defines the standardized YAML frontmatter format to be used across all markdown files in the LifeOS PARA system. This ensures consistency, enables automated processing, and supports comprehensive metadata-driven navigation.

## Master Frontmatter Template

```yaml
---
title: "[Descriptive Title in Title Case]"
subtitle: "[Optional secondary descriptor]"
type: "[note|project|area|resource|journal|routine|template]"
category: "[PARA Category: projects|areas|resources|archives]"
subcategory: "[Optional: personal|family|professional|home|life-management|knowledge|tools|media]"
status: "[Active|Completed|Paused|Archived|Fleeting|Permanent]"
priority: "[High|Medium|Low|Critical]"
created: "YYYY-MM-DD"
last_modified: "YYYY-MM-DD"
last_accessed: "YYYY-MM-DD"
tags: 
  - "tag1"
  - "tag2"
  - "tag3"
related_files:
  - "file-name-without-extension"
  - "another-related-file"
related_projects:
  - "project-name-1"
  - "project-name-2"
related_areas:
  - "area-name-1"
  - "area-name-2"
linked_files:
  - "[[file-name-without-extension]]"
  - "[[another-linked-file]]"
author: "[Creator Name/ID]"
source: "[Source information if applicable]"
version: "[File version number]"
completeness: "[0-100% - estimated completion]"
time_estimate: "[Time in minutes/hours/days]"
context: "[Brief contextual information]"
goal: "[Primary objective or purpose]"
location: "[Physical or digital location]"
equipment: "[Required tools or materials]"
next_action: "[Immediate next step if applicable]"
deadline: "[YYYY-MM-DD if applicable]"
permissions: "[public|private|restricted]"
language: "en"
encoding: "utf-8"
word_count: "[Auto-calculated]"
reading_time: "[Auto-calculated in minutes]"
difficulty: "[Beginner|Intermediate|Advanced]"
effort_level: "[1-5 scale]"
energy_required: "[1-5 scale]"
frequency: "[Daily|Weekly|Monthly|As Needed|One-time]"
dependencies: 
  - "dependency-1"
  - "dependency-2"
outsourced: "[Yes|No - indicates if work is done by others]"
iteration: "[Version or iteration number]"
review_date: "[YYYY-MM-DD for periodic review]"
archive_date: "[YYYY-MM-DD if applicable]"
custom_fields:
  field1: "value1"
  field2: "value2"
---
```

## Type-Specific Frontmatter Variants

### Project Files
```yaml
---
title: "Project Name"
type: "project"
category: "projects"
status: "[Active|Completed|Paused|Archived]"
priority: "[High|Medium|Low|Critical]"
created: "YYYY-MM-DD"
last_modified: "YYYY-MM-DD"
deadline: "YYYY-MM-DD"
completion_percentage: "[0-100%]"
team_members: 
  - "member1"
  - "member2"
project_phase: "[Planning|Development|Review|Complete]"
budget: "[Financial information]"
resources_needed:
  - "resource1"
  - "resource2"
deliverables:
  - "deliverable1"
  - "deliverable2"
milestones:
  - milestone1: "YYYY-MM-DD"
  - milestone2: "YYYY-MM-DD"
risk_level: "[Low|Medium|High]"
success_metrics:
  - "metric1"
  - "metric2"
---
```

### Area Files
```yaml
---
title: "Life Area Name"
type: "area"
category: "areas"
status: "[Active|Needs Attention|Well Maintained]"
created: "YYYY-MM-DD"
last_modified: "YYYY-MM-DD"
review_frequency: "[Weekly|Monthly|Quarterly]"
standards: 
  - "standard1"
  - "standard2"
kpis: 
  - "kpi1"
  - "kpi2"
stakeholders: 
  - "stakeholder1"
  - "stakeholder2"
maintenance_tasks:
  - task1
  - task2
quality_threshold: "[Minimum acceptable level]"
last_review: "YYYY-MM-DD"
next_review: "YYYY-MM-DD"
improvement_areas:
  - "area1"
  - "area2"
---
```

### Resource Files
```yaml
---
title: "Resource Title"
type: "resource"
category: "resources"
status: "[Active|Verified|Needs Review|Outdated]"
created: "YYYY-MM-DD"
last_modified: "YYYY-MM-DD"
source_url: "[URL if applicable]"
source_type: "[Book|Article|Video|Course|Website|Video|Other]"
author: "[Author name]"
publisher: "[Publisher/Source]"
publication_date: "YYYY-MM-DD"
credibility: "[High|Medium|Low]"
relevance: "[High|Medium|Low]"
usage_count: "[Number of times referenced]"
last_used: "YYYY-MM-DD"
next_review: "YYYY-MM-DD"
rating: "[1-5 stars]"
summary: "[Brief description]"
key_concepts:
  - "concept1"
  - "concept2"
actionable_items:
  - "action1"
  - "action2"
verified: "[Yes|No]"
verification_date: "YYYY-MM-DD"
---
```

### Journal Files
```yaml
---
title: "Journal Entry YYYY-MM-DD"
type: "journal"
category: "resources"
date: "YYYY-MM-DD"
mood: "[1-10 scale]"
energy: "[1-10 scale]"
focus: "[1-10 scale]"
weather: "[Weather conditions]"
location: "[Current location]"
people_interacted: 
  - "person1"
  - "person2"
key_events:
  - "event1"
  - "event2"
learnings: 
  - "learning1"
  - "learning2"
challenges:
  - "challenge1"
  - "challenge2"
gratitude:
  - "gratitude1"
  - "gratitude2"
  - "gratitude3"
tomorrow_focus:
  - "focus1"
  - "focus2"
sleep_quality: "[1-10 scale]"
exercise: "[Yes|No and details]"
meals: "[Brief description]"
productivity: "[1-10 scale]"
---
```

## Field Definitions and Usage Guidelines

### Required Fields (Universal)
- **title**: Clear, descriptive title in Title Case
- **type**: One of the predefined content types
- **category**: PARA category alignment
- **created**: Original creation date in ISO format
- **last_modified**: Most recent edit date in ISO format
- **status**: Current state of the content

### Recommended Fields
- **tags**: 3-7 relevant tags for classification
- **related_files**: Direct connections to other files
- **priority**: For actionable content
- **completeness**: For tracking progress

### Optional Fields
- Use custom_fields section for specific needs
- Add fields as needed for specialized content types
- Maintain backward compatibility

## Validation Rules

### Date Format
- **ISO 8601**: YYYY-MM-DD (e.g., 2025-11-11)
- **Datetime**: YYYY-MM-DDTHH:MM:SSZ (for precise timestamps)

### Status Values
- **Projects**: Active, Completed, Paused, Archived
- **Areas**: Active, Needs Attention, Well Maintained
- **Resources**: Active, Verified, Needs Review, Outdated
- **Notes**: Fleeting, Permanent

### Priority Scale
- **Critical**: Must be addressed immediately
- **High**: Important but not urgent
- **Medium**: Standard priority
- **Low**: Nice to have, time permitting

## Implementation Examples

### Example 1: Active Project
```yaml
---
title: "LifeOS Web Application Development"
type: "project"
category: "projects"
status: "Active"
priority: "High"
created: "2025-10-15"
last_modified: "2025-11-11"
deadline: "2025-12-31"
completion_percentage: 65
tags:
  - "development"
  - "web-application"
  - "lifeos"
  - "ui-design"
related_files:
  - "web-ui-chat-architecture"
  - "unified-web-ui-design"
related_areas:
  - "technology-skills"
  - "career-development"
next_action: "Implement user authentication system"
budget: "$0 - Open source"
---
```

### Example 2: Life Area
```yaml
---
title: "Family and Marriage"
type: "area"
category: "areas"
status: "Active"
created: "2025-01-01"
last_modified: "2025-11-10"
review_frequency: "Weekly"
standards:
  - "Daily quality time"
  - "Weekly date night"
  - "Monthly family meetings"
kpis:
  - "Relationship satisfaction (1-10)"
  - "Communication quality"
  - "Conflict resolution time"
stakeholders:
  - "spouse"
  - "children"
maintenance_tasks:
  - "Weekly relationship check-ins"
  - "Monthly planning sessions"
last_review: "2025-11-03"
next_review: "2025-11-17"
tags:
  - "family"
  - "marriage"
  - "relationships"
  - "parenting"
---
```

## Automation and Processing

### Automated Field Population
- **word_count**: Calculate from content length
- **reading_time**: Based on word count (200 WPM average)
- **last_accessed**: Track file access timestamps
- **usage_count**: Increment on file references

### Validation Scripts
- Frontmatter completeness check
- Date format validation
- Status value verification
- Tag consistency validation
- Link integrity verification

### Search and Filter Support
- Full-text search across all fields
- Tag-based filtering
- Date range queries
- Status-based views
- Priority-based sorting

## Migration Strategy

### Backward Compatibility
- Existing files without frontmatter will be enhanced
- Old metadata formats will be converted
- No content will be lost during migration

### Incremental Implementation
- New files use full frontmatter standard
- Existing files enhanced during review cycles
- Automated tools assist in standardization

---
*Standard Version: 1.0*
*Created: 2025-11-11*
*Last Updated: 2025-11-11*