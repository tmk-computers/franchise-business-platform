"""
Pitch Deck PowerPoint Generator
===============================
Generates an editable 10-slide PowerPoint presentation (.pptx)
for client franchise pitch packages using python-pptx.
"""

import sys
import os
import argparse
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.dml.color import RGBColor


def create_deck(client_name: str, output_path: str):
    prs = Presentation()
    # Set slide dimensions to 16:9 widescreen
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)

    blank_layout = prs.slide_layouts[6]

    color_primary = RGBColor(31, 73, 125)    # Navy Blue
    color_accent = RGBColor(227, 108, 10)     # Orange
    color_dark = RGBColor(38, 38, 38)        # Charcoal
    color_light_bg = RGBColor(242, 244, 247) # Soft Gray
    color_white = RGBColor(255, 255, 255)

    def add_header(slide, title_text, category_text="FRANCHISE OPPORTUNITY"):
        # Header banner
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.5), Inches(11.7), Inches(1.2))
        tf = title_box.text_frame
        tf.word_wrap = True

        p_cat = tf.paragraphs[0]
        p_cat.text = category_text.upper()
        p_cat.font.size = Pt(11)
        p_cat.font.bold = True
        p_cat.font.color.rgb = color_accent

        p_title = tf.add_paragraph()
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = color_primary

    # -------------------------------------------------------------
    # Slide 1: Title Slide
    # -------------------------------------------------------------
    s1 = prs.slides.add_slide(blank_layout)
    bg1 = s1.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.333), Inches(7.5)) # 1 = rectangle
    bg1.fill.solid()
    bg1.fill.fore_color.rgb = color_primary
    bg1.line.color.rgb = color_primary

    tbox1 = s1.shapes.add_textbox(Inches(1.5), Inches(2.0), Inches(10.3), Inches(3.5))
    tf1 = tbox1.text_frame
    tf1.word_wrap = True

    p1 = tf1.paragraphs[0]
    p1.text = client_name.upper()
    p1.font.size = Pt(18)
    p1.font.bold = True
    p1.font.color.rgb = color_accent

    p2 = tf1.add_paragraph()
    p2.text = "Software Franchise Partnership"
    p2.font.size = Pt(40)
    p2.font.bold = True
    p2.font.color.rgb = color_white

    p3 = tf1.add_paragraph()
    p3.text = "High-Margin B2B Software Business Opportunity | FOFO Model | India Expansion"
    p3.font.size = Pt(18)
    p3.font.color.rgb = RGBColor(210, 225, 245)

    # -------------------------------------------------------------
    # Slide 2: The Opportunity & Market Need
    # -------------------------------------------------------------
    s2 = prs.slides.add_slide(blank_layout)
    add_header(s2, "The Market Opportunity: Digital Transformation in Bharat")
    box2 = s2.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.8))
    tf2 = box2.text_frame
    tf2.word_wrap = True
    bullets2 = [
        "1. Rapid Digitization: Over 1.5 million schools, 63 million MSMEs, and thousands of real estate properties across India are migrating from pen-and-paper to digital systems.",
        "2. The Local Trust Deficit: Centralized SaaS giants fail in Tier-2, Tier-3, and rural talukas because local institutions demand face-to-face demonstrations, local language support, and in-person relationship trust.",
        "3. The Franchise Advantage: Combining institutional-grade software engineering with local entrepreneurial sales presence captures market share faster than direct sales teams.",
        "4. High Recurring Value: Software is mission-critical. Once a school or business adopts an ERP, annual renewal rates exceed 85%, compounding franchise earnings year after year."
    ]
    for b in bullets2:
        p = tf2.add_paragraph()
        p.text = b
        p.font.size = Pt(15)
        p.font.color.rgb = color_dark
        p.space_after = Pt(14)

    # -------------------------------------------------------------
    # Slide 3: Six High-Demand Software Products
    # -------------------------------------------------------------
    s3 = prs.slides.add_slide(blank_layout)
    add_header(s3, "Comprehensive Software Portfolio Across 6 Verticals")
    products_info = [
        ("1. School / College ERP", "Automated student attendance, fees, exams, report cards & parent mobile app. Price: ₹60,000 / yr."),
        ("2. Invoicing App + Web", "GST-compliant invoicing, inventory, payment links & accounting for retail & MSMEs. Price: ₹12,000 / yr."),
        ("3. OMR Evaluation Software", "High-speed optical mark recognition for competitive exams, coaching centers & colleges. Price: ₹25,000 / yr."),
        ("4. Property Management ERP", "Society maintenance billing, tenant verification, visitor security & asset management. Price: ₹75,000 / yr."),
        ("5. DevOps Automation Platform", "Cloud server deployment, continuous delivery & IT infrastructure orchestration. Price: ₹90,000 / yr."),
        ("6. Sales CRM Platform", "Lead tracking, WhatsApp messaging integration & field sales performance management. Price: ₹35,000 / yr.")
    ]
    for idx, (p_title, p_desc) in enumerate(products_info):
        col_offset = Inches(0.8) if idx < 3 else Inches(6.8)
        row_offset = Inches(2.0 + (idx % 3) * 1.6)
        pbox = s3.shapes.add_textbox(col_offset, row_offset, Inches(5.7), Inches(1.4))
        ptf = pbox.text_frame
        ptf.word_wrap = True
        pp1 = ptf.paragraphs[0]
        pp1.text = p_title
        pp1.font.size = Pt(15)
        pp1.font.bold = True
        pp1.font.color.rgb = color_primary
        pp2 = ptf.add_paragraph()
        pp2.text = p_desc
        pp2.font.size = Pt(12)
        pp2.font.color.rgb = color_dark

    # -------------------------------------------------------------
    # Slide 4: The FOFO Model & Responsibilities
    # -------------------------------------------------------------
    s4 = prs.slides.add_slide(blank_layout)
    add_header(s4, "FOFO Operating Model: Clear Separation of Powers")
    
    # Left box: Franchisee
    box_fee = s4.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(5.6), Inches(4.8))
    tf_fee = box_fee.text_frame
    tf_fee.word_wrap = True
    p_fee_h = tf_fee.paragraphs[0]
    p_fee_h.text = "FRANCHISE OWNER RESPONSIBILITIES"
    p_fee_h.font.size = Pt(16)
    p_fee_h.font.bold = True
    p_fee_h.font.color.rgb = color_accent
    f_bullets = [
        "• Establish & operate a local commercial sales office.",
        "• Hire & manage at least 1 dedicated salesperson.",
        "• Conduct local networking, field marketing & outreach.",
        "• Coordinate qualified customer software demonstrations.",
        "• Build long-term client trust & lead renewal follow-ups."
    ]
    for b in f_bullets:
        p = tf_fee.add_paragraph()
        p.text = b
        p.font.size = Pt(14)
        p.font.color.rgb = color_dark
        p.space_after = Pt(10)

    # Right box: Franchisor
    box_sor = s4.shapes.add_textbox(Inches(6.8), Inches(2.0), Inches(5.6), Inches(4.8))
    tf_sor = box_sor.text_frame
    tf_sor.word_wrap = True
    p_sor_h = tf_sor.paragraphs[0]
    p_sor_h.text = "FRANCHISOR (TMK) RESPONSIBILITIES"
    p_sor_h.font.size = Pt(16)
    p_sor_h.font.bold = True
    p_sor_h.font.color.rgb = color_primary
    s_bullets = [
        "• 100% Core software development & feature updates.",
        "• Cloud hosting, server uptime & data security.",
        "• End-to-end software deployment & customer implementation.",
        "• Technical demo co-presentation & sales enablement.",
        "• Level-2 & Level-3 customer support & bug resolution.",
        "• Central customer billing & commission settlement."
    ]
    for b in s_bullets:
        p = tf_sor.add_paragraph()
        p.text = b
        p.font.size = Pt(14)
        p.font.color.rgb = color_dark
        p.space_after = Pt(10)

    # -------------------------------------------------------------
    # Slide 5: Revenue-Sharing & Unit Economics
    # -------------------------------------------------------------
    s5 = prs.slides.add_slide(blank_layout)
    add_header(s5, "Generous 40:60 Commercial Revenue Share")
    box5 = s5.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.8))
    tf5 = box5.text_frame
    tf5.word_wrap = True
    rev_points = [
        "• 40% Franchisee Revenue Share: On every new software license and annual subscription renewal closed within your territory.",
        "• 60% Franchisor Retained Share: Reinvested into continuous product R&D, central cloud hosting, and technical implementation teams.",
        "• Low Break-Even Hurdle: Closing just 1 to 2 software deals per month clears all local office rent and salesperson salaries.",
        "• Cash Flow Example (School ERP @ ₹60,000 net):",
        "    - Franchisee Commission: ₹24,000 per closed school contract.",
        "    - Close 3 deals/month = ₹72,000 Gross Commission Income.",
        "    - Monthly Fixed Costs = ₹35,000 (Rent + Salary + Ops).",
        "    - Net Monthly Operating Cash Flow: ₹37,000+ positive EBITDA."
    ]
    for r in rev_points:
        p = tf5.add_paragraph()
        p.text = r
        p.font.size = Pt(14)
        p.font.color.rgb = color_dark
        p.space_after = Pt(8)

    # -------------------------------------------------------------
    # Slide 6: Franchise Investment Requirements
    # -------------------------------------------------------------
    s6 = prs.slides.add_slide(blank_layout)
    add_header(s6, "Initial Capital Investment & Setup Schedule")
    box6 = s6.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.8))
    tf6 = box6.text_frame
    tf6.word_wrap = True
    inv_points = [
        "• Promotional Joining Fee: ₹25,000 per product (₹1,50,000 for full 6-product territory rights).",
        "• Regular Standard Fee: ₹50,000 per product (post-promotional phase).",
        "• Office Infrastructure & IT Setup: ~₹1,26,000 (Rental deposit, branding, laptops, furniture).",
        "• Working Capital Reserve: ~₹1,40,000 (Mandatory 4-month solvency reserve covering rent & salary).",
        "• Total All-Inclusive Capital Outlay: ~₹3,26,000 to ₹4,16,000.",
        "• Payback Horizon: Capital recovered within 11 months in Base Case scenario."
    ]
    for i in inv_points:
        p = tf6.add_paragraph()
        p.text = i
        p.font.size = Pt(15)
        p.font.color.rgb = color_dark
        p.space_after = Pt(12)

    # -------------------------------------------------------------
    # Slide 7: Territory Allocation Strategy
    # -------------------------------------------------------------
    s7 = prs.slides.add_slide(blank_layout)
    add_header(s7, "Taluka-Based Territory Protection & Exclusivity")
    box7 = s7.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.8))
    tf7 = box7.text_frame
    tf7.word_wrap = True
    ter_points = [
        "• Clear Administrative Boundaries: Territories are assigned by Taluka/Tehsil or District, avoiding arbitrary radius conflicts.",
        "• Protected Deal Registration: Leads logged in the central CRM are locked to the originating franchisee for 90 days.",
        "• Wave 1 Priority Markets: Initial rollout focuses on high-density education and commercial talukas across Western and Central India.",
        "• Expansion Rights: High-performing Tier-1 franchisees receive first right of refusal for adjacent unoccupied talukas."
    ]
    for t in ter_points:
        p = tf7.add_paragraph()
        p.text = t
        p.font.size = Pt(15)
        p.font.color.rgb = color_dark
        p.space_after = Pt(14)

    # -------------------------------------------------------------
    # Slide 8: Franchise Onboarding Journey
    # -------------------------------------------------------------
    s8 = prs.slides.add_slide(blank_layout)
    add_header(s8, "Structured 30-Day Onboarding & Launch Roadmap")
    box8 = s8.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.8))
    tf8 = box8.text_frame
    tf8.word_wrap = True
    steps = [
        "• Days 1–5: Due diligence, commercial sign-off, territory assignment & CRM credentials provisioning.",
        "• Days 6–15: Intensive 10-day Product Certification Bootcamp & Recorded Demo Training.",
        "• Days 16–22: Office branding inspection, sales collateral delivery & initial prospect mapping.",
        "• Days 23–30: Official territory launch; first 10 joint customer discovery meetings co-led by franchisor demo specialist."
    ]
    for s in steps:
        p = tf8.add_paragraph()
        p.text = s
        p.font.size = Pt(15)
        p.font.color.rgb = color_dark
        p.space_after = Pt(14)

    # -------------------------------------------------------------
    # Slide 9: Three-Year Network Growth Vision
    # -------------------------------------------------------------
    s9 = prs.slides.add_slide(blank_layout)
    add_header(s9, "Three-Year Expansion Vision & Network Scaling")
    box9 = s9.shapes.add_textbox(Inches(0.8), Inches(2.0), Inches(11.7), Inches(4.8))
    tf9 = box9.text_frame
    tf9.word_wrap = True
    growth = [
        "• Year 1 (Wave 1): 15 Operating Franchise Units across Western India | Focus on School ERP & Invoicing App.",
        "• Year 2 (Wave 2): 45 Operating Franchise Units across 4 States | Expansion into Property ERP & CRM.",
        "• Year 3 (Wave 3): 100+ Nationwide Operating Units | Regional Area Developers appointed.",
        "• Long-Term Value: Franchisees build an asset-backed recurring cash flow machine through compounded annual renewals."
    ]
    for g in growth:
        p = tf9.add_paragraph()
        p.text = g
        p.font.size = Pt(15)
        p.font.color.rgb = color_dark
        p.space_after = Pt(14)

    # -------------------------------------------------------------
    # Slide 10: Call to Action & Contact
    # -------------------------------------------------------------
    s10 = prs.slides.add_slide(blank_layout)
    bg10 = s10.shapes.add_shape(1, Inches(0), Inches(0), Inches(13.333), Inches(7.5))
    bg10.fill.solid()
    bg10.fill.fore_color.rgb = color_primary
    bg10.line.color.rgb = color_primary

    tbox10 = s10.shapes.add_textbox(Inches(1.5), Inches(2.0), Inches(10.3), Inches(3.5))
    tf10 = tbox10.text_frame
    tf10.word_wrap = True

    c1 = tf10.paragraphs[0]
    c1.text = "JOIN THE FRANCHISE NETWORK"
    c1.font.size = Pt(18)
    c1.font.bold = True
    c1.font.color.rgb = color_accent

    c2 = tf10.add_paragraph()
    c2.text = "Secure Your Taluka Territory Today"
    c2.font.size = Pt(36)
    c2.font.bold = True
    c2.font.color.rgb = color_white

    c3 = tf10.add_paragraph()
    c3.text = f"Contact TMK Franchise Operations | Web: tmkitsolutions.com | Email: franchise@tmkitsolutions.com\nStrictly Confidential — Prepared for Prospective Commercial Partners"
    c3.font.size = Pt(16)
    c3.font.color.rgb = RGBColor(210, 225, 245)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    prs.save(output_path)
    print(f"PowerPoint pitch deck saved successfully to: {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate franchise opportunity pitch deck")
    parser.add_argument("--client", default="tmk-it-solutions", help="Client slug")
    parser.add_argument("--client-name", default="TMK IT Solutions LLP", help="Client legal name")
    parser.add_argument("--output", default=None, help="Output file path")
    args = parser.parse_args()

    output_path = args.output or os.path.join("clients", args.client, "presentations", "franchise-opportunity-pitch-deck.pptx")
    create_deck(args.client_name, output_path)


if __name__ == "__main__":
    main()
