export default (state, action) => {
  switch (action.type) {
    case "UPDATE_STATES":
      return {
        results: {
          prediction: action.payload.prediction,
          confidence: action.payload.confidence
        },
        uploadInfo: {
          file: action.payload.file,
          filename: action.payload.filename
        },
        uploaded: action.payload.uploaded
      };
    default:
      return state;
  }
};
