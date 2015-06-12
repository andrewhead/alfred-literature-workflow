#! /usr/bin/env python
# encoding: utf-8

from __future__ import unicode_literals
import logging
from feedback import Feedback
import argparse
import config


logging.basicConfig(level=logging.INFO, format="%(message)s")
RECENT_COUNT = 10


TITLES = (
    "Doing Psychology Experiments.",
    "Methodology Matters: Doing Research in the Behavioral and Social Sciences.",
    "An Ethnographic Approach to Design.",
    "Research Methods in Human-Computer Interaction.",
    "Contextual Design: Defining Customer-Centered Systems (notes)",
    "The Model Human Processor: An Engineering Model of Human Performance.",
    "The Humane Interface: New Directions for Designing Interactive Systems.",
    "Perception, Increase Appeal, Make Better Design Decisions, and Teach through Design.",
    "Input Technologies and Techniques.",
    "User Technology: From Pointing to Pondering.",
    "Readings in Information Visualization: Using Vision to Think.",
    "CHCI Models, Theories, and Frameworks: Toward a Multidisciplinary Science.",
    "Direct Manipulation Interfaces.",
    "Developing User Interfaces.",
    "Search User Interfaces.",
    "Designing Visual Interfaces.",
    "Designing the User Interface: Strategies for Effective Human-Computer Interaction.",
    "Task-Centered User Interface Design.",
    "Universal Principles of Design, Revised and Updated: 125 Ways to Enhance Usability, Influence",
    "Beyond Being There.",
    "The Structure of Scientific Revolutions.",
    "The Design of Everyday Things.",
    "How to Conduct a Heuristic Evaluation.",
    "#23 - How to Run a Design Critique.",
    "#35 - How to Give and Receive Criticism.",
    "Visual Guide to Storyboarding",
    "Designing Apple Help.",
    "10 Usability Heuristics for User Interface Design.",
    "Novel interfaces",
    "Multi-Touch Systems That I Have Known and Loved.",
    "GOMS.",
    "Measuring the User Experience: Collecting, Analyzing, and Presenting Usability Metrics.",
    "Practical Guide to Controlled Experiments on the Web: Listen to Your Customers Not to the Hippo.",  # noqa
    "TurKit: Human Computation Algorithms on Mechanical Turk.",
    "Everyone Can Write Better (and You Are No Exception).",
    "Evaluating User Interface Systems Research.",
    "Yesterday’s Tomorrows: Notes on Ubiquitous Computing’s Dominant Vision",
    "Past, Present, and Future of User Interface Software Tools.",
    "The Computer for the 21st Century.",
    "Building Interactive Systems: Principles for Human-Computer Interaction.",
    "What Do Prototypes Prototype.",
    "Sketching User Experiences: Getting the Design Right and the Right Design: Getting the Design Right and the Right Design",  # noqa
    "A Morphological Analysis of the Design Space of Input Devices.",
    "Deep Shot: A Framework for Migrating Tasks across Devices Using Mobile Phone Cameras.",
    "Groupware and Social Dynamics: Eight Challenges for Developers.",
    "How Bodies Matter: Five Themes for Interaction Design.",
    "Principles of Mixed-Initiative User Interfaces.",
    "Tangible Bits: Towards Seamless Interfaces Between People, Bits and Atoms.",
    "The Art of Innovation: Lessons in Creativity from IDEO, America’s Leading Design Firm.",
    "DART: A Toolkit for Rapid Design Exploration of Augmented Reality Experiences.",
    "The Need for Web Design Standards",
    "Ten Myths of Multimodal Interaction.",
    "Rapid Development of User Interfaces on Cluster-Driven Wall Displays with jBricks.",
    "Prototyping for Tiny Fingers.",
    "Haptic Techniques for Media Control.",
    "Organic User Interfaces.",
    "Designing Games with a Purpose.",
    "Fitt’s Law: Modeling Movement in Time in HCI",
    "Extending Fitts’ Law to Two-Dimensional Tasks.",
    "Human Computation: A Survey and Taxonomy of a Growing Field.",
    "On Distinguishing Epistemic from Pragmatic Action.",
    "User Acceptance of Information Technology: System Characteristics, User Perceptions and Behavioral Impacts.",  # noqa
    "When the Wait Isn’t so Bad: The Interacting Effects of Website Delay, Familiarity, and Breadth.",  # noqa
    "A Survey of Software Learnability: Metrics, Methodologies and Guidelines.",
    "Zoetrope: Interacting with the Ephemeral Web.",
    "You’ve Been Warned: An Empirical Study of the Effectiveness of Web Browser Phishing Warnings.",
    "The Anatomy of a Large-Scale Social Search Engine.",
    "Conditioned-Safe Ceremonies and a User Study of an Application to Web Authentication.",
    "Avaaj Otalo: A Field Study of an Interactive Voice Forum for Small Farmers in Rural India.",
    "The Psychology of Security.",
    "Generating Photo Manipulation Tutorials by Demonstration.",
    "Code Bubbles: A Working Set-Based Interface for Code Understanding and Maintenance.",
    "Improving the Performance of Motor-Impaired Users with Automatically-Generated, Ability-Based Interfaces.",  # noqa
    "Video Object Annotation, Navigation, and Composition.",
    "The Bubble Cursor: Enhancing Target Acquisition by Dynamic Resizing of the Cursor’s Activation Area.",  # noqa
    "Low-Cost Multi-Touch Sensing Through Frustrated Total Internal Reflection.",
    "Edit Wear and Read Wear.",
    "Design Galleries: A General Approach to Setting Parameters for Computer Graphics and Animation.",  # noqa
    "Non-Invasive Interactive Visualization of Dynamic Architectural Environments.",
    "Revision: Automated Classification, Analysis and Redesign of Chart Images.",
    "The ModelCraft Framework: Capturing Freehand Annotations and Edits to Facilitate the 3D Model Design Process Using a Digital Pen.",  # noqa
    "The Audio Notebook: Paper and Pen Interaction with Structured Speech.",
    "Using a Depth Camera As a Touch Sensor.",
    "Interacting with Paper on the DigitalDesk.",
    "Sikuli: Using GUI Screenshots for Search and Automation.",
    "Combining Multiple Depth Cameras and Projectors for Interactions On, above and between Surfaces.",  # noqa
    "Depth-Sensing Video Cameras for 3D Tangible Tabletop Interaction.",
)


feedback = Feedback()
add = lambda t: feedback.add_item(t, subtitle="Set current document to %s" % t, arg=t)
added = []


def add_default_titles(query):
    for t in TITLES:
        if query.lower() in t.lower() and t not in added:
            added.append(t)
            add(t)


def add_previous_titles(query, notesfile):
    with open(notesfile) as nfile:
        titles = [l.split('\t')[0] for l in nfile.readlines()]
        for t in titles:
            if query.lower() in t.lower() and t not in added:
                added.append(t)
                add(t)


def add_recent_titles(notesfile):
    with open(notesfile) as nfile:
        titles = [l.split('\t')[0] for l in nfile.readlines()]
        titles.reverse()
        titles_uniq = []
        [titles_uniq.append(t) for t in titles if t not in titles_uniq]
        [add(t) for t in titles_uniq[:RECENT_COUNT]]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Get prelim titles that match a certain name, ignoring case.')
    parser.add_argument('--query', help='partial title of work')
    args = parser.parse_args()

    query = None if args.query is None or args.query == '' else args.query

    if query is not None:
        add_default_titles(query)

    notesfile = config.get_option('notesfile')
    if notesfile is not None:
        if query is not None:
            add_previous_titles(query, notesfile)
        else:
            add_recent_titles(notesfile)

    if query is not None and query not in added:
        add(query)

    print feedback
