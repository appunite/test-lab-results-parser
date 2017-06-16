# Basic Firebase Test Lab results parser 

Parse .xml files to specified json files

## Usage
- `SOURCE_PATH`: Path to directory with tests results
- `DESTINATION_PATH`: Path to directory where json file will be stored
- `VERSION_NAME`: Build version name
- `VERSION_CODE`: Build version code
- `CI_PIPELINE_ID`: Pipeline

```
- python testlab.py --source "${SOURCE_PATH}" --destination "${DESTINATION_PATH}" --build "${VERSION_NAME}" --version "${VERSION_CODE}" --pipeline "${CI_PIPELINE_ID}" --commiter "${GITLAB_USER_EMAIL}"
```
