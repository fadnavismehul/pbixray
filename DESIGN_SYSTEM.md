# Grab Duxton Design System Implementation

## Overview

This document outlines the implementation of Grab Duxton Design principles in the PBIXRay application. The design system follows Grab's brand guidelines and creates a cohesive, accessible, and modern user interface.

## Design Tokens

### Color Palette

#### Primary Colors (Grab Brand)
- **Primary Green**: `#00B14F` (Grab's signature green, PMS 355C equivalent)
- **Primary Light**: `#33C473`
- **Primary Lighter**: `#66D797`
- **Primary Lightest**: `#E6F7ED`
- **Primary Dark**: `#008A3B`
- **Primary Darker**: `#006428`

#### Secondary Colors
- **Secondary Blue**: `#0066CC` (Digital blue for interactive elements)
- **Secondary Light**: `#3385D6`
- **Secondary Lighter**: `#66A3E0`
- **Secondary Lightest**: `#E6F2FF`

#### Semantic Colors
- **Success**: `#28A745` with light variant `#D4EDDA`
- **Warning**: `#FFC107` with light variant `#FFF3CD`
- **Error**: `#DC3545` with light variant `#F8D7DA`
- **Info**: `#17A2B8` with light variant `#D1ECF1`

#### Neutral Colors
- **Text Primary**: `#212529`
- **Text Secondary**: `#6C757D`
- **Text Muted**: `#ADB5BD`
- **Background Light**: `#F8F9FA`
- **Border Default**: `#DEE2E6`

### Typography

- **Font Family**: Inter (with system font fallbacks)
- **Font Sizes**: Scale from 12px (0.75rem) to 32px (2rem)
- **Font Weights**: 300-700 range for different text hierarchies

### Spacing

Consistent spacing scale using rem units:
- **XS**: 0.25rem (4px)
- **SM**: 0.5rem (8px)
- **MD**: 1rem (16px)
- **LG**: 1.5rem (24px)
- **XL**: 2rem (32px)
- **XXL**: 3rem (48px)

### Border Radius

- **Small**: 0.25rem (4px)
- **Medium**: 0.5rem (8px)
- **Large**: 0.75rem (12px)
- **X-Large**: 1rem (16px)

### Shadows

Layered shadow system for depth and hierarchy:
- **Small**: Subtle 1px shadow for minimal elevation
- **Medium**: Standard component shadow
- **Large**: Modal and overlay shadows
- **X-Large**: High-elevation elements

## Design Principles Applied

### 1. **Consistent Visual Hierarchy**
- Clear typography scale with consistent font weights
- Proper use of white space and padding
- Color-coded sections for better content organization

### 2. **Accessibility**
- High contrast ratios for text readability
- Semantic color usage (green for success, red for errors)
- Clear focus states and interactive elements

### 3. **Brand Consistency**
- Grab's signature green as the primary color
- Professional and clean aesthetic
- Consistent iconography and visual elements

### 4. **User Experience**
- Loading states with branded spinners
- Clear call-to-action buttons
- Intuitive navigation and content organization
- Responsive design considerations

## Component Styling

### Header
- Gradient background using primary colors
- Prominent branding with PBIXRay title
- Clean, centered layout

### File Upload
- Branded upload area with primary color accents
- Clear visual feedback for drag-and-drop
- Helpful tooltips and instructions

### Metrics Cards
- Clean white cards with subtle shadows
- Primary color highlights for values
- Consistent spacing and typography

### Buttons
- Primary buttons use Grab green
- Secondary buttons use digital blue
- Hover states with smooth transitions
- Consistent border radius and typography

### Data Tables
- Clean borders and spacing
- Accessible color contrasts
- Responsive design
- Collapsible sections for better organization

### Messages and Alerts
- Color-coded based on message type
- Left border accent for visual hierarchy
- Consistent padding and typography

## Implementation Notes

### CSS Custom Properties
The design system uses CSS custom properties (variables) for consistent theming:

```css
:root {
    --primary-color: #00B14F;
    --secondary-color: #0066CC;
    --text-primary: #212529;
    /* ... additional variables */
}
```

### Streamlit Integration
- Custom CSS applied via `st.markdown()` with `unsafe_allow_html=True`
- Component-specific styling using Streamlit class selectors
- Responsive design considerations for different screen sizes

### Font Loading
- Inter font loaded from Google Fonts
- System font fallbacks for performance
- Proper font weights for different text elements

## Usage Guidelines

### Colors
- Use primary green for main actions and branding
- Use secondary blue for download and secondary actions
- Use semantic colors consistently (green for success, red for errors)
- Maintain proper contrast ratios for accessibility

### Typography
- Use consistent font weights for hierarchy
- Maintain readable line heights and spacing
- Use appropriate font sizes for different content types

### Spacing
- Follow the spacing scale for consistent layouts
- Use adequate white space for readability
- Maintain consistent margins and padding

### Interactive Elements
- Provide clear hover and focus states
- Use consistent button sizing and spacing
- Include helpful tooltips and instructions

## Accessibility Considerations

- **Color Contrast**: All text meets WCAG 2.1 AA standards
- **Focus Management**: Clear focus indicators for keyboard navigation
- **Semantic Markup**: Proper heading hierarchy and semantic elements
- **Screen Reader Support**: Meaningful labels and descriptions

## Future Enhancements

1. **Dark Mode Support**: Implement dark theme variants
2. **Component Library**: Extract reusable components
3. **Animation System**: Add micro-interactions and transitions
4. **Mobile Optimization**: Enhanced mobile experience
5. **Theming API**: Allow for brand customization

## Files Modified

- `design_tokens.py`: Core design token definitions
- `streamlit_app.py`: Main application with styling applied
- `DESIGN_SYSTEM.md`: This documentation file

---

*This design system implementation follows Grab's brand guidelines while adapting to the specific needs of the PBIXRay application. The system prioritizes usability, accessibility, and brand consistency.*