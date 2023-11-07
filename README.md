# demo-ai-tgis
Text Generation Inference Server with DevSpaces Code-Llama assistant

## Work in progress...

![tgis-demo](images/text-generation-inference.jpg "text-generation-inference")

### What's Needed
- [Openshift with a worker node that has (4) NVIDIA T4 GPUs](https://github.com/redhat-na-ssa/demo-ai-gitops-catalog)

Deploy the model server.
```
oc new-project tgi
oc apply -k resources/base
```

Visit the [Swagger docs](https://tgis-tgi.apps.ocp.sandbox1873.opentlc.com/docs/).

Deploy the Gradio test chat app.

```
export INFERENCE_URL = Gradio app route
```

Fire up DevSpaces and let the Llama help you code!

Need to add the correct `devfile` and instructions here.