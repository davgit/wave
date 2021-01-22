// Copyright 2020 H2O.ai, Inc.
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

import React from 'react'
import { render } from '@testing-library/react'
import { XMessageBar, MessageBar } from './message_bar'
import { initializeIcons } from '@fluentui/react'

const
  name = 'message_bar',
  messagebarProps: MessageBar = { name, text: name }

describe('MessageBar.tsx', () => {
  beforeAll(() => initializeIcons())

  it('Does not render data-test attr', () => {
    const { container } = render(<XMessageBar model={{}} />)
    expect(container.querySelectorAll('[data-test]')).toHaveLength(0)
  })

  it('Renders data-test attr', () => {
    const { queryByTestId } = render(<XMessageBar model={messagebarProps} />)
    expect(queryByTestId(name)).toBeInTheDocument()
  })

  it('Does not display message bar when visible is false', () => {
    const { queryByTestId } = render(<XMessageBar model={{ ...messagebarProps, visible: false }} />)
    expect(queryByTestId(name)).toBeInTheDocument()
    expect(queryByTestId(name)).not.toBeVisible()
  })
})