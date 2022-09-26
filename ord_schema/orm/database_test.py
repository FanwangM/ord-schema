# Copyright 2022 Open Reaction Database Project Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Tests for ord_schema.orm.database."""
from sqlalchemy import select
from ord_schema.orm.mappers import Compound, CompoundIdentifier, Reaction, ReactionInput


def test_orm(test_session):
    query = (
        select(Reaction)
        .join(ReactionInput)
        .join(Compound)
        .join(CompoundIdentifier)
        .where(CompoundIdentifier.type == "SMILES", CompoundIdentifier.value == "c1ccccc1CCC(O)C")
    )
    results = test_session.execute(query)
    assert len(results.fetchall()) == 20
