# StudyMate LMS — Portfolio Testing Checklist

Use a private browser window for the final review.

## Public access

- [ ] The live URL loads successfully.
- [ ] Login with the documented demo credentials works.
- [ ] Refreshing a nested route does not return a 404 page.
- [ ] Logging out returns to the login page.

## Read-only protection

- [ ] Dashboard and list pages load.
- [ ] Creating a record returns a read-only warning and does not change data.
- [ ] Editing a record returns a read-only warning and does not change data.
- [ ] Deleting a record returns a read-only warning and does not change data.
- [ ] The demo account cannot sign in to Django `/admin/`.

## Manager workflow

- [ ] Dashboard
- [ ] Users and students
- [ ] Grades, groups, and subjects
- [ ] Courses and syllabuses
- [ ] Academic years and terms
- [ ] Timetables, rooms, and time bounds
- [ ] Marks and final marks
- [ ] Awards, communities, and announcements

## Presentation

- [ ] No broken images or empty error panels are visible.
- [ ] Browser console has no critical errors.
- [ ] GitHub About section contains the live demo URL.
- [ ] README links work.
- [ ] Six screenshots are added under `docs/screenshots/`.
