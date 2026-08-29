# Evidence for Social Media Studio

## PROBE 1
- Ingest sample post
- Generate platform variants
- Validate with profile rules

## PROBE 2
- Force rule-breaking content
- Validation blocks it before review

## PROBE 3
- Try to schedule unapproved draft
- API returns 4xx with clear error

## PROBE 4
- Approve a variant and schedule it
- Publish to configured target and record external URL

## PROBE 5
- Simulate worker retry or restart
- History records one successful post only

## PROBE 6
- Swap adapter configuration
- Same campaign publishes through mock without logic changes
