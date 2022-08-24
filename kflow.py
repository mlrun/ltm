# Copyright 2021 Iguazio
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import mlrun
from kfp import dsl

funcs = {}
project = mlrun.projects.pipeline_context.project
iris_data = 'https://s3.wasabisys.com/iguazio/data/iris/iris.data.raw.csv'
default_pkg_class = "sklearn.linear_model.LogisticRegression"

@dsl.pipeline(
    name="Demo training pipeline",
    description="Shows how to use mlrun."
)
def kfpipeline(model_pkg_class=default_pkg_class, build=0):

    # if build=True, build the function image before the run
    with dsl.Condition(build==1) as build_cond:
        funcs["prep-data"].deploy_step(skip_deployed=True)

    # run a local data prep function
    prep_data = funcs["prep-data"].as_step(name='prep_data',
                                           inputs={'source_url': project.get_artifact_uri("data")},
                                           outputs=["cleaned_data"]).after(build_cond)
